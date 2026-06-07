import streamlit as st
import pandas as pd
import sys
sys.path.append(".")
from services.db_service import get_sorted_complaints, clear_all_complaints
from utils.helpers import get_urgency_color, get_sentiment_color, get_urgency_emoji, get_sentiment_emoji

def show():
    st.markdown("""
        <div style='text-align:center; padding: 20px 0'>
            <h1>📊 Support Team Dashboard</h1>
            <p style='color: gray; font-size: 16px'>Complaints sorted by urgency — highest priority first</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    complaints = get_sorted_complaints()

    # Stats row
    total = len(complaints)
    critical = len([c for c in complaints if c.get("urgency_label") == "Critical"])
    high = len([c for c in complaints if c.get("urgency_label") == "High"])
    negative = len([c for c in complaints if c.get("sentiment") == "Negative"])

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📋 Total Complaints", total)
    col2.metric("🔴 Critical", critical)
    col3.metric("🟠 High Priority", high)
    col4.metric("😡 Negative Sentiment", negative)

    st.divider()

    # Refresh and clear buttons
    col1, col2 = st.columns([4, 1])
    with col1:
        st.subheader("📌 Live Complaint Feed")
    with col2:
        if st.button("🗑️ Clear All", type="secondary"):
            clear_all_complaints()
            st.rerun()

    if not complaints:
        st.info("📭 No complaints yet. Waiting for submissions...")
        return

    # Display each complaint as a card
    for c in complaints:
        urgency_color = get_urgency_color(c.get("urgency_label", "Medium"))
        sentiment_color = get_sentiment_color(c.get("sentiment", "Neutral"))

        with st.container():
            st.markdown(f"""
                <div style='
                    border-left: 5px solid {urgency_color};
                    background: #1e1e2e;
                    padding: 16px 20px;
                    border-radius: 8px;
                    margin-bottom: 12px;
                '>
                    <div style='display:flex; justify-content:space-between; align-items:center;'>
                        <div>
                            <span style='font-size:18px; font-weight:700;'>#{c.get("id")} — {c.get("name")}</span>
                            <span style='color:gray; font-size:13px; margin-left:10px;'>{c.get("email")}</span>
                        </div>
                        <div>
                            <span style='
                                background:{urgency_color}22;
                                color:{urgency_color};
                                padding: 4px 10px;
                                border-radius: 20px;
                                font-size: 13px;
                                font-weight: 600;
                                margin-right: 8px;
                            '>{get_urgency_emoji(c.get("urgency_label"))} {c.get("urgency_label")} — {c.get("urgency_score")}/10</span>
                            <span style='
                                background:{sentiment_color}22;
                                color:{sentiment_color};
                                padding: 4px 10px;
                                border-radius: 20px;
                                font-size: 13px;
                                font-weight: 600;
                            '>{get_sentiment_emoji(c.get("sentiment"))} {c.get("sentiment")} {c.get("sentiment_symbol")}</span>
                        </div>
                    </div>
                    <p style='margin: 10px 0 4px 0; color: #ccc;'>{c.get("complaint")}</p>
                    <p style='color: gray; font-size: 12px;'>📋 {c.get("summary")} &nbsp;|&nbsp; 🕐 {c.get("timestamp")}</p>
                </div>
            """, unsafe_allow_html=True)

    st.divider()

    # Table view
    st.subheader("📊 Summary Table")
    df = pd.DataFrame(complaints)
    if not df.empty:
        display_df = df[["id", "name", "email", "urgency_score", "urgency_label", "sentiment", "summary", "timestamp"]].copy()
        display_df.columns = ["ID", "Name", "Email", "Score", "Priority", "Sentiment", "Summary", "Time"]
        st.dataframe(display_df, use_container_width=True, hide_index=True)
