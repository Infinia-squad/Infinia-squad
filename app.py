import streamlit as st
import sys
sys.path.append(".")

st.set_page_config(
    page_title="Complaint Prioritizer",
    page_icon="🆘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom dark theme styling
st.markdown("""
    <style>
        .stApp { background-color: #0f1117; }
        .stSidebar { background-color: #1a1d2e; }
        .stButton > button {
            background-color: #6c8cf5;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
        }
        .stButton > button:hover { background-color: #5a7ae0; }
        div[data-testid="metric-container"] {
            background: #1a1d2e;
            border: 1px solid #2a2d3e;
            border-radius: 10px;
            padding: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown("""
        <div style='text-align:center; padding: 20px 0'>
            <h2>🆘 Complaint<br>Prioritizer</h2>
            <p style='color:gray; font-size:13px'>AI-Powered Support System</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "Navigate",
        ["📝 Submit Complaint", "📊 Support Dashboard"],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("""
        <div style='color:gray; font-size:12px; text-align:center;'>
            <p>Powered by</p>
            <p>🤖 Groq AI (LLaMA 3)</p>
            <p>Built with Streamlit</p>
        </div>
    """, unsafe_allow_html=True)

# Page routing
if page == "📝 Submit Complaint":
    from pages.user_form import show
    show()
elif page == "📊 Support Dashboard":
    from pages.dashboard import show
    show()
