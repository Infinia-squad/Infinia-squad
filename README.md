# 🆘 AI-Powered Customer Complaint Prioritization System

An intelligent customer support system that uses **Groq AI (LLaMA 3)** to automatically analyze, classify and prioritize customer complaints in real-time.

## 🚀 Features
- AI sentiment analysis (Positive / Neutral / Negative)
- Urgency scoring (1-10) with priority labels (Low / Medium / High / Critical)
- Live support dashboard sorted by urgency
- Real-time complaint feed with color coded cards
- Summary table for quick overview

## 🛠 Tech Stack
- **Frontend & UI** — Streamlit
- **AI Brain** — Groq API (LLaMA 3 8B)
- **Backend** — Python
- **Storage** — JSON file

## ⚙️ Setup

1. Clone the repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your Groq API key in `.env`:
```
GROQ_API_KEY=your_groq_api_key_here
```

4. Run the app:
```bash
streamlit run app.py
```

## 📁 Project Structure
```
complaint-prioritizer/
├── app.py                  # Main entry point
├── pages/
│   ├── user_form.py        # Customer complaint form
│   └── dashboard.py        # Support team dashboard
├── services/
│   ├── groq_service.py     # Groq AI analysis
│   └── db_service.py       # Data storage
├── data/
│   ├── complaints.json     # Stored complaints
│   └── sample_data.py      # Test data
├── utils/
│   └── helpers.py          # Helper functions
├── .env                    # API keys
└── requirements.txt
```

## 🔑 Get Groq API Key
1. Go to https://console.groq.com
2. Sign up for free
3. Create an API key
4. Paste it in your `.env` file
