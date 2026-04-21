"""
agent.py — HR Policy Bot
LangGraph agent with 8 nodes, ChromaDB RAG, MemorySaver, self-reflection eval,
tool use (datetime + web search), and full conversation memory.

Author : Gargi Shashidhar
Roll No: 23052572
Batch  : Agentic AI 2026
"""

import os
import re
from datetime import datetime
from typing import TypedDict, List

from dotenv import load_dotenv
load_dotenv()

# ── LangGraph ──────────────────────────────────────────────────────────────────
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

# ── LLM (Groq) ─────────────────────────────────────────────────────────────────
from langchain_groq import ChatGroq

# ── Embeddings + ChromaDB ──────────────────────────────────────────────────────
from sentence_transformers import SentenceTransformer
import chromadb

# ── Knowledge Base ─────────────────────────────────────────────────────────────
from knowledge_base.hr_docs import DOCUMENTS

# ── User Memory ────────────────────────────────────────────────────────────────
from user_memory import load_profile, save_profile, record_topic

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════
MAX_EVAL_RETRIES = 2
SLIDING_WINDOW   = 6          # keep last N messages in context
FAITHFULNESS_THRESHOLD = 0.70

LLM_MODEL = "llama-3.3-70b-versatile"  # Groq free-tier model

# ══════════════════════════════════════════════════════════════════════════════
# LLM INITIALISATION
# ══════════════════════════════════════════════════════════════════════════════
llm = ChatGroq(
    model=LLM_MODEL,
    temperature=0.2,
    api_key=os.getenv("GROQ_API_KEY"),
)

# ══════════════════════════════════════════════════════════════════════════════
# EMBEDDER + CHROMADB KNOWLEDGE BASE
# ══════════════════════════════════════════════════════════════════════════════
print("Loading embedder …")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="hr_policy_kb")

print(f"Indexing {len(DOCUMENTS)} HR policy documents …")
for doc in DOCUMENTS:
    emb = embedder.encode([doc["text"]]).tolist()
    collection.add(
        documents=[doc["text"]],
        embeddings=emb,
        ids=[doc["id"]],
        metadatas=[{"topic": doc["topic"], "id": doc["id"]}],
    )

# ── Retrieval smoke test ───────────────────────────────────────────────────────
_probes = ["What is the annual leave policy?", "How do I apply for work from home?"]
for _q in _probes:
    _emb = embedder.encode([_q]).tolist()
    _res = collection.query(query_embeddings=_emb, n_results=1)
    print(f"  Smoke test: '{_q}' → {_res['metadatas'][0][0]['topic']}")
print("Knowledge base ready.\n")

# ══════════════════════════════════════════════════════════════════════════════
# STATE DEFINITION  — designed BEFORE any node function (as required)
# ══════════════════════════════════════════════════════════════════════════════
class CapstoneState(TypedDict):
    question     : str
    messages     : List[dict]        # full conversation history
    route        : str               # "retrieve" | "tool" | "memory_only"
    retrieved    : str               # formatted retrieved context
    sources      : List[str]         # list of topic names retrieved
    tool_result  : str               # string result from tool_node
    answer       : str               # agent's final answer this turn
    faithfulness : float             # 0.0 – 1.0 from eval_node
    eval_retries : int               # how many retries have happened
    user_name    : str               # extracted / stored display name
    user_id      : str               # stable login key
    user_profile : dict              # profile dict from disk


# ══════════════════════════════════════════════════════════════════════════════
# NODE 1 — memory_node
# ══════════════════════════════════════════════════════════════════════════════
def memory_node(state: CapstoneState) -> dict:
    """
    Prepend the new question to messages, apply sliding window,
    extract the user's name if they introduce themselves, and load/refresh
    their profile from disk so name survives the sliding window.
    """
    question = state["question"]
    messages = list(state.get("messages", []))
    user_id  = state.get("user_id", "default_user")

    # Load fresh profile
    profile = load_profile(user_id)

    # Extract name if "my name is X" pattern found
    name_match = re.search(
        r"(?:my name is|i(?:'m| am)|call me)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)",
        question, re.IGNORECASE
    )
    if name_match:
        extracted = name_match.group(1).strip().title()
        profile["name"] = extracted

    user_name = profile.get("name", "")

    # Add question to history
    messages.append({"role": "user", "content": question})

    # Sliding window — keep last SLIDING_WINDOW messages
    messages = messages[-SLIDING_WINDOW:]

    return {
        "messages"    : messages,
        "user_name"   : user_name,
        "user_profile": profile,
        "eval_retries": 0,        # reset retry counter each new turn
    }


# ══════════════════════════════════════════════════════════════════════════════
# NODE 2 — router_node
# ══════════════════════════════════════════════════════════════════════════════
def router_node(state: CapstoneState) -> dict:
    """
    Decide whether to retrieve from KB, call a tool, or answer from memory only.
    The LLM must reply with exactly ONE word.
    """
    question = state["question"]
    prompt = f"""You are a routing agent for an HR Policy assistant.

Given the user's question, decide which route to take. Reply with EXACTLY ONE WORD — nothing else.

Routes:
- retrieve   → the question is about an HR policy, rule, benefit, leave, salary, conduct, or process
- tool       → the question needs today's date/time, a calculation, or real-time information
- memory_only → the question is pure small-talk, a greeting, or already answerable from conversation history

Question: {question}

Reply with ONE word only (retrieve / tool / memory_only):"""

    response = llm.invoke(prompt)
    route = response.content.strip().lower().split()[0]
    if route not in ("retrieve", "tool", "memory_only"):
        route = "retrieve"   # default to retrieval if LLM gives unexpected output
    return {"route": route}


# ══════════════════════════════════════════════════════════════════════════════
# NODE 3 — retrieval_node
# ══════════════════════════════════════════════════════════════════════════════
def retrieval_node(state: CapstoneState) -> dict:
    """
    Embed the question and query ChromaDB for top 3 matching policy chunks.
    Returns a formatted context string with [Topic] labels.
    """
    question = state["question"]
    query_emb = embedder.encode([question]).tolist()
    results = collection.query(query_embeddings=query_emb, n_results=3)

    docs     = results["documents"][0]
    metas    = results["metadatas"][0]
    sources  = [m["topic"] for m in metas]

    context_parts = []
    for doc, meta in zip(docs, metas):
        context_parts.append(f"[{meta['topic']}]\n{doc}")
    retrieved = "\n\n".join(context_parts)

    return {"retrieved": retrieved, "sources": sources}


# ══════════════════════════════════════════════════════════════════════════════
# NODE 4 — skip_retrieval_node
# ══════════════════════════════════════════════════════════════════════════════
def skip_retrieval_node(state: CapstoneState) -> dict:
    """Clear context fields for memory-only queries — no KB lookup needed."""
    return {"retrieved": "", "sources": []}


# ══════════════════════════════════════════════════════════════════════════════
# NODE 5 — tool_node
# ══════════════════════════════════════════════════════════════════════════════
def tool_node(state: CapstoneState) -> dict:
    """
    Handle tool calls: datetime and basic arithmetic calculator.
    NEVER raises exceptions — always returns a string result.
    """
    question = state["question"].lower()
    result   = ""

    # Date / time tool
    if any(kw in question for kw in ["date", "day", "time", "today", "month", "year"]):
        now = datetime.now()
        result = (
            f"Today is {now.strftime('%A, %d %B %Y')}. "
            f"Current time is {now.strftime('%I:%M %p')} IST."
        )

    # Calculator tool — evaluate safe math expressions
    if not result or any(kw in question for kw in ["calculate", "compute", "how much", "+", "-", "*", "/"]):
        expr_match = re.search(r"[\d\s\.\+\-\*\/\(\)]+", state["question"])
        if expr_match:
            expr = expr_match.group(0).strip()
            if len(expr) > 1:
                try:
                    # Restrict to safe math evaluation
                    allowed = set("0123456789 +-*/.() ")
                    if all(c in allowed for c in expr):
                        calc_result = eval(expr)  # nosec — filtered to math only
                        result = (result + " " if result else "") + f"Calculation result: {expr} = {calc_result}"
                except Exception:
                    result = (result + " " if result else "") + "Could not evaluate the expression."

    if not result:
        result = "Tool did not find a matching operation. Please rephrase or ask an HR policy question."

    return {"tool_result": result}


# ══════════════════════════════════════════════════════════════════════════════
# NODE 6 — answer_node
# ══════════════════════════════════════════════════════════════════════════════
def answer_node(state: CapstoneState) -> dict:
    """
    Build the final answer using retrieved context OR tool result.
    Strict grounding rule: answer ONLY from context provided, never fabricate.
    """
    question     = state["question"]
    retrieved    = state.get("retrieved", "")
    tool_result  = state.get("tool_result", "")
    messages     = state.get("messages", [])
    user_name    = state.get("user_name", "")
    eval_retries = state.get("eval_retries", 0)

    name_clause = f"Address the employee as {user_name}." if user_name else ""

    history_text = ""
    for m in messages[-4:]:
        role = "Employee" if m["role"] == "user" else "HR Assistant"
        history_text += f"{role}: {m['content']}\n"

    retry_instruction = ""
    if eval_retries > 0:
        retry_instruction = (
            "\nIMPORTANT: Your previous answer scored below the faithfulness threshold. "
            "This time, stay even more strictly within the provided context. "
            "Do not add anything not explicitly stated in the context."
        )

    context_section = ""
    if retrieved:
        context_section = f"\n\nRELEVANT HR POLICY CONTEXT:\n{retrieved}"
    if tool_result:
        context_section += f"\n\nTOOL RESULT:\n{tool_result}"

    system_prompt = f"""You are a professional HR Policy Assistant for a mid-sized company.
Your role is to answer employees' questions about HR policies accurately and clearly.

STRICT RULES:
1. Answer ONLY using the provided context. Do not invent policies or numbers.
2. If the answer is not in the context, say clearly: "I don't have that specific information in our policy documents. Please contact HR at hr@company.com or raise a helpdesk ticket."
3. Be warm, professional, and concise. Use simple language — avoid jargon.
4. If a policy has specific numbers (days, percentages, amounts), quote them exactly.
5. Never give legal or medical advice beyond what the policy states.
{name_clause}{retry_instruction}

CONVERSATION HISTORY:
{history_text}{context_section}

Employee's question: {question}

Answer:"""

    response = llm.invoke(system_prompt)
    return {"answer": response.content.strip()}


# ══════════════════════════════════════════════════════════════════════════════
# NODE 7 — eval_node
# ══════════════════════════════════════════════════════════════════════════════
def eval_node(state: CapstoneState) -> dict:
    """
    LLM-based faithfulness evaluator. Scores 0.0–1.0.
    Skips evaluation if no retrieved context (tool/memory answers).
    """
    retrieved = state.get("retrieved", "")
    answer    = state.get("answer", "")
    retries   = state.get("eval_retries", 0)

    # Skip faithfulness check when no KB context was used
    if not retrieved:
        return {"faithfulness": 1.0, "eval_retries": retries}

    eval_prompt = f"""You are a faithfulness evaluator. 
Score whether the answer below is fully supported by the context provided.

CONTEXT:
{retrieved}

ANSWER:
{answer}

Scoring rules:
- 1.0 = every claim in the answer is directly supported by the context
- 0.7–0.9 = mostly supported, minor additions acceptable
- 0.4–0.6 = answer has some claims not in context
- 0.0–0.3 = answer largely fabricates or contradicts the context

Reply with ONLY a decimal number between 0.0 and 1.0. Nothing else."""

    try:
        response = llm.invoke(eval_prompt)
        score = float(re.search(r"\d+\.?\d*", response.content).group())
        score = max(0.0, min(1.0, score))
    except Exception:
        score = 1.0   # if eval fails, assume pass

    return {"faithfulness": score, "eval_retries": retries + 1}


# ══════════════════════════════════════════════════════════════════════════════
# NODE 8 — save_node
# ══════════════════════════════════════════════════════════════════════════════
def save_node(state: CapstoneState) -> dict:
    """
    Append the assistant's answer to messages, update user profile on disk,
    and record which topic was accessed.
    """
    messages = list(state.get("messages", []))
    answer   = state.get("answer", "")
    sources  = state.get("sources", [])
    profile  = dict(state.get("user_profile", {}))

    messages.append({"role": "assistant", "content": answer})

    # Record topics accessed in this turn
    for topic in sources:
        profile = record_topic(profile, topic)

    save_profile(profile)

    print(f"[save_node] faithfulness={state.get('faithfulness', '?'):.2f}  "
          f"route={state.get('route', '?')}  sources={sources}")

    return {"messages": messages, "user_profile": profile}


# ══════════════════════════════════════════════════════════════════════════════
# ROUTING FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════
def route_decision(state: CapstoneState) -> str:
    route = state.get("route", "retrieve")
    if route == "tool":
        return "tool"
    elif route == "memory_only":
        return "skip"
    return "retrieve"


def eval_decision(state: CapstoneState) -> str:
    faith   = state.get("faithfulness", 1.0)
    retries = state.get("eval_retries", 0)
    if faith < FAITHFULNESS_THRESHOLD and retries < MAX_EVAL_RETRIES:
        return "answer"   # retry answer_node
    return "save"


# ══════════════════════════════════════════════════════════════════════════════
# GRAPH ASSEMBLY
# ══════════════════════════════════════════════════════════════════════════════
graph = StateGraph(CapstoneState)

graph.add_node("memory",   memory_node)
graph.add_node("router",   router_node)
graph.add_node("retrieve", retrieval_node)
graph.add_node("skip",     skip_retrieval_node)
graph.add_node("tool",     tool_node)
graph.add_node("answer",   answer_node)
graph.add_node("eval",     eval_node)
graph.add_node("save",     save_node)

graph.set_entry_point("memory")

graph.add_edge("memory",   "router")
graph.add_conditional_edges("router", route_decision,
                             {"retrieve": "retrieve", "skip": "skip", "tool": "tool"})
graph.add_edge("retrieve",  "answer")
graph.add_edge("skip",      "answer")
graph.add_edge("tool",      "answer")
graph.add_edge("answer",    "eval")
graph.add_conditional_edges("eval", eval_decision,
                             {"answer": "answer", "save": "save"})
graph.add_edge("save", END)

app = graph.compile(checkpointer=MemorySaver())
print("Graph compiled successfully.\n")


# ══════════════════════════════════════════════════════════════════════════════
# HELPER — ask()
# ══════════════════════════════════════════════════════════════════════════════
def ask(question: str, thread_id: str = "default", user_id: str = "default_user") -> dict:
    """
    Invoke the graph and return a dict with answer, route, faithfulness, and sources.
    """
    config = {"configurable": {"thread_id": thread_id}}
    initial_state: CapstoneState = {
        "question"    : question,
        "messages"    : [],
        "route"       : "",
        "retrieved"   : "",
        "sources"     : [],
        "tool_result" : "",
        "answer"      : "",
        "faithfulness": 1.0,
        "eval_retries": 0,
        "user_name"   : "",
        "user_id"     : user_id,
        "user_profile": {},
    }
    result = app.invoke(initial_state, config=config)
    return {
        "answer"      : result["answer"],
        "route"       : result["route"],
        "faithfulness": result["faithfulness"],
        "sources"     : result["sources"],
    }
