import streamlit as st
import sys
sys.path.append(".")
from services.groq_service import analyze_complaint
from services.db_service import save_complaint
from utils.helpers import get_urgency_emoji, get_sentiment_emoji

def show():
    st.markdown("""
        <div style='text-align:center; padding: 20px 0'>
            <h1>🆘 Customer Support Portal</h1>
            <p style='color: gray; font-size: 16px'>Submit your complaint and we'll prioritize it immediately</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    with st.form("complaint_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("👤 Full Name", placeholder="John Doe")
        with col2:
            email = st.text_input("📧 Email / User ID", placeholder="john@example.com")

        complaint = st.text_area(
            "📝 Describe your issue",
            placeholder="Please describe your complaint in detail...",
            height=150
        )

        submitted = st.form_submit_button("🚀 Submit Complaint", use_container_width=True)

    if submitted:
        if not name or not email or not complaint:
            st.error("⚠️ Please fill in all fields before submitting.")
            return

        with st.spinner("🤖 AI is analyzing your complaint..."):
            analysis = analyze_complaint(complaint)

        complaint_data = {
            "name": name,
            "email": email,
            "complaint": complaint,
            "sentiment": analysis.get("sentiment"),
            "sentiment_symbol": analysis.get("sentiment_symbol"),
            "urgency_score": analysis.get("urgency_score"),
            "urgency_label": analysis.get("urgency_label"),
            "summary": analysis.get("summary"),
        }

        save_complaint(complaint_data)

        st.success("✅ Your complaint has been submitted successfully!")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                "Sentiment",
                f"{get_sentiment_emoji(analysis.get('sentiment'))} {analysis.get('sentiment')}"
            )
        with col2:
            st.metric(
                "Urgency Score",
                f"{analysis.get('urgency_score')} / 10"
            )
        with col3:
            st.metric(
                "Priority Level",
                f"{get_urgency_emoji(analysis.get('urgency_label'))} {analysis.get('urgency_label')}"
            )

        st.info(f"📋 **Summary:** {analysis.get('summary')}")
        st.caption("Our support team has been notified and will contact you shortly.")
