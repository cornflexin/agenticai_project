"""
capstone_streamlit.py — HR Policy Bot UI
Streamlit chat interface with login, multi-turn memory, and sidebar info.

Author : Gargi Shashidhar
Roll No: 23052572
Batch  : Agentic AI 2026

Run with:  streamlit run capstone_streamlit.py
"""

import streamlit as st
import uuid
from datetime import datetime

# ── Page config (must be first Streamlit call) ─────────────────────────────
st.set_page_config(
    page_title="HR Policy Bot",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load agent once per server lifetime ────────────────────────────────────
@st.cache_resource
def load_agent():
    from agent import app, embedder, collection, ask
    return app, embedder, collection, ask

_app, _embedder, _collection, ask = load_agent()

# ══════════════════════════════════════════════════════════════════════════
# SESSION STATE INITIALISATION
# ══════════════════════════════════════════════════════════════════════════
if "logged_in" not in st.session_state:
    st.session_state.logged_in   = False
if "user_name" not in st.session_state:
    st.session_state.user_name   = ""
if "user_id" not in st.session_state:
    st.session_state.user_id     = ""
if "thread_id" not in st.session_state:
    st.session_state.thread_id   = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages    = []
if "session_start" not in st.session_state:
    st.session_state.session_start = datetime.now().strftime("%d %b %Y, %I:%M %p")

# ══════════════════════════════════════════════════════════════════════════
# CUSTOM CSS
# ══════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
    /* Chat bubbles */
    .user-bubble {
        background: #0077B6;
        color: white;
        padding: 12px 16px;
        border-radius: 18px 18px 4px 18px;
        margin: 6px 0;
        max-width: 75%;
        float: right;
        clear: both;
        font-size: 15px;
        line-height: 1.5;
    }
    .bot-bubble {
        background: #F0F4F8;
        color: #1A1A2E;
        padding: 12px 16px;
        border-radius: 18px 18px 18px 4px;
        margin: 6px 0;
        max-width: 80%;
        float: left;
        clear: both;
        font-size: 15px;
        line-height: 1.5;
        border-left: 4px solid #0077B6;
    }
    .chat-container { overflow: hidden; margin-bottom: 8px; }
    .source-tag {
        font-size: 11px;
        color: #666;
        margin-top: 4px;
        font-style: italic;
    }
    /* Header */
    .main-header {
        background: linear-gradient(135deg, #0077B6, #023E8A);
        color: white;
        padding: 20px 28px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .main-header h1 { margin: 0; font-size: 26px; }
    .main-header p  { margin: 4px 0 0 0; font-size: 14px; opacity: 0.85; }
    /* Login card */
    .login-card {
        background: white;
        padding: 32px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        max-width: 480px;
        margin: 60px auto;
    }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════
# LOGIN SCREEN
# ══════════════════════════════════════════════════════════════════════════
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class='main-header'>
          <h1>🏢 HR Policy Bot</h1>
          <p>Your 24/7 HR policy assistant — instant answers, zero wait time.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("login_form"):
            st.subheader("Welcome! Please introduce yourself.")
            name = st.text_input("Your Name", placeholder="e.g. Priya Sharma")
            emp_id = st.text_input("Employee ID (optional)", placeholder="e.g. EMP1042")
            dept = st.text_input("Department (optional)", placeholder="e.g. Engineering")
            submitted = st.form_submit_button("Start Chat →", use_container_width=True)

            if submitted:
                if not name.strip():
                    st.error("Please enter your name to continue.")
                else:
                    st.session_state.user_name = name.strip().title()
                    user_id = emp_id.strip() if emp_id.strip() else name.strip().lower().replace(" ", "_")
                    st.session_state.user_id = user_id
                    st.session_state.logged_in = True
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": (
                            f"Hello {st.session_state.user_name}! 👋 I'm your HR Policy Assistant. "
                            "I can help you with questions about leave policies, salary, work from home, "
                            "performance appraisal, reimbursements, and more.\n\n"
                            "What would you like to know today?"
                        ),
                        "sources": [],
                    })
                    st.rerun()
    st.stop()

# ══════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown(f"### 👤 {st.session_state.user_name}")
    st.caption(f"Session started: {st.session_state.session_start}")
    st.divider()

    st.markdown("**📚 Topics I can help with:**")
    topics = [
        "🗓️ Annual & Casual Leave",
        "🤒 Sick Leave",
        "👶 Maternity / Paternity Leave",
        "🏠 Work From Home Policy",
        "💰 Salary & Payroll",
        "📈 Performance Appraisal",
        "📋 Code of Conduct",
        "🚪 Resignation & Notice Period",
        "🧾 Reimbursements",
        "🆕 Onboarding & Probation",
        "🎓 Training & Development",
        "📣 Grievance Redressal",
    ]
    for t in topics:
        st.markdown(f"<small>{t}</small>", unsafe_allow_html=True)

    st.divider()

    st.markdown("**💡 Try asking:**")
    st.markdown("""
    <small>
    • How many annual leave days do I get?<br>
    • What is the WFH policy?<br>
    • How is my salary structured?<br>
    • What is the notice period?<br>
    • How do I claim travel reimbursement?
    </small>
    """, unsafe_allow_html=True)

    st.divider()

    if st.button("🔄 New Conversation", use_container_width=True):
        st.session_state.thread_id = str(uuid.uuid4())
        st.session_state.messages  = [{
            "role": "assistant",
            "content": (
                f"New conversation started! Hi again, {st.session_state.user_name}. "
                "What HR policy question can I help you with?"
            ),
            "sources": [],
        }]
        st.rerun()

    if st.button("🚪 Logout", use_container_width=True):
        for key in ["logged_in", "user_name", "user_id", "thread_id", "messages", "session_start"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

    st.divider()
    st.caption("📧 HR Helpdesk: hr@company.com")
    st.caption("☎️ HR Hotline: +91-80-1234-5678")

# ══════════════════════════════════════════════════════════════════════════
# MAIN CHAT AREA
# ══════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class='main-header'>
  <h1>🏢 HR Policy Bot</h1>
  <p>Ask me anything about company policies — leave, salary, appraisals, WFH, and more.</p>
</div>
""", unsafe_allow_html=True)

# Display chat history
for msg in st.session_state.messages:
    with st.container():
        if msg["role"] == "user":
            st.markdown(
                f"<div class='chat-container'>"
                f"<div class='user-bubble'>🧑 {msg['content']}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )
        else:
            sources_html = ""
            if msg.get("sources"):
                src_text = " · ".join(msg["sources"][:2])
                sources_html = f"<div class='source-tag'>📄 Sources: {src_text}</div>"
            st.markdown(
                f"<div class='chat-container'>"
                f"<div class='bot-bubble'>🤖 {msg['content']}{sources_html}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

# ── Input ─────────────────────────────────────────────────────────────────
with st.form("chat_form", clear_on_submit=True):
    col_input, col_btn = st.columns([5, 1])
    with col_input:
        user_input = st.text_input(
            "Ask your HR question …",
            placeholder="e.g. How many sick leave days do I have per year?",
            label_visibility="collapsed",
        )
    with col_btn:
        send = st.form_submit_button("Send →", use_container_width=True)

if send and user_input.strip():
    question = user_input.strip()

    # Add user message to display
    st.session_state.messages.append({"role": "user", "content": question, "sources": []})

    with st.spinner("Looking up policy …"):
        try:
            result = ask(
                question=question,
                thread_id=st.session_state.thread_id,
                user_id=st.session_state.user_id,
            )
            answer  = result["answer"]
            sources = result.get("sources", [])
        except Exception as e:
            answer  = (
                "I encountered an issue processing your request. "
                "Please try again or contact HR directly at hr@company.com."
            )
            sources = []
            st.error(f"Error: {e}")

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources,
    })
    st.rerun()
