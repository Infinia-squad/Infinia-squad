import streamlit as st
import sys
sys.path.append(".")

st.set_page_config(
    page_title="Complaint Prioritizer",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
        .stRadio > label { color: #9499b0 !important; }
        .stDivider { border-color: #2a2d3e; }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
        <div style='text-align:center; padding: 20px 0'>
            <h2 style='color:#e8eaf0; font-size:18px; margin-bottom:4px;'>Complaint Prioritizer</h2>
            <p style='color:#9499b0; font-size:12px; margin:0;'>AI-Powered Support System</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "Navigate",
        ["Submit Complaint", "Support Dashboard"],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("""
        <div style='color:#9499b0; font-size:12px; text-align:center; padding: 8px 0;'>
            <p style='margin:4px 0;'>Powered by Groq AI (LLaMA 3)</p>
            <p style='margin:4px 0;'>Built with Streamlit</p>
            <p style='margin:10px 0 4px 0; color:#6c8cf5; font-weight:600;'>Infinia Squad</p>
            <p style='margin:0; font-size:11px;'></p>
        </div>
    """, unsafe_allow_html=True)

if page == "Submit Complaint":
    from pages.user_form import show
    show()
elif page == "Support Dashboard":
    from pages.dashboard import show
    show()