# HR Policy Bot

**Gargi Shashidhar | Roll No: 23052572 | Agentic AI 2026**

A conversational HR Policy assistant built with LangGraph, ChromaDB, and Groq. Employees can ask questions about leave, salary, WFH rules, appraisals, notice periods, and more — and get accurate, grounded answers any time of day.

---

## How to run it

**Step 1 — Install dependencies**
```
pip install -r requirements.txt
```

**Step 2 — Add your Groq API key**
```
cp .env.example .env
```
Open `.env` and paste your key from console.groq.com (free account works fine).

**Step 3 — Launch the app**
```
streamlit run capstone_streamlit.py
```
Opens at http://localhost:8501

**Or open the notebook**
```
jupyter notebook day13_capstone.ipynb
```
Run Kernel → Restart & Run All.

---

## Project files

```
hr_policy_bot/
├── agent.py                  ← LangGraph agent (8 nodes, eval loop, tools)
├── capstone_streamlit.py     ← Streamlit chat UI
├── day13_capstone.ipynb      ← Capstone notebook with all 8 parts
├── user_memory.py            ← Employee profile persistence
├── knowledge_base/
│   ├── __init__.py
│   └── hr_docs.py            ← 12 HR policy documents
├── profiles/                 ← Auto-created when the app first runs
├── requirements.txt
├── .env.example              ← Rename to .env, add GROQ_API_KEY
└── HR_Policy_Bot_Documentation_Gargi_Shashidhar.pdf
```

---

## What the agent does

- Answers questions about 12 HR policy topics from a curated knowledge base
- Remembers the employee's name across the whole session (and across sessions)
- Routes date/time and arithmetic questions to a dedicated tool instead of guessing
- Scores its own answers for faithfulness before showing them — low scores trigger a retry
- Admits when it doesn't know something and points the employee to the HR helpdesk
