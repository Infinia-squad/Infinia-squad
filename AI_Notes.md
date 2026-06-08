# Complaint Prioritizer
### AI-Powered Customer Complaint Prioritization System
**Team: Infinia Squad | Infinite Computer Solutions**

---

## Overview

Complaint Prioritizer is a real-time AI-powered support tool that automatically analyzes incoming customer complaints, detects sentiment, and assigns an urgency score — so support teams always know which issues to resolve first.

---

## Features

- AI sentiment analysis — Positive, Neutral, or Negative
- Urgency scoring from 1 to 10 with priority labels (Low / Medium / High / Critical)
- Live support dashboard sorted by urgency — highest priority first
- Real-time complaint feed with color-coded cards
- Summary table with CSV export and correct timestamps
- Clean professional dark theme UI

---

## Architecture Overview

```
complaint-prioritizer/
│
├── app.py                        # Main Streamlit entry point & navigation
│
├── pages/
│   ├── user_form.py              # Customer complaint submission form
│   └── dashboard.py             # Live support team dashboard
│
├── services/
│   ├── groq_service.py          # Groq API connection & AI analysis logic
│   └── db_service.py            # Save & fetch complaints (JSON storage)
│
├── data/
│   ├── complaints.json          # Live complaint storage
│   └── sample_data.py           # 10 realistic test complaints
│
├── utils/
│   └── helpers.py               # Color and label helper functions
│
├── .streamlit/
│   └── config.toml              # Hides default Streamlit sidebar nav
│
├── .env                         # API keys (not committed to GitHub)
├── .gitignore                   # Excludes .env and pycache
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

### Flow

```
User submits complaint
        ↓
Groq API (LLaMA 3.3-70b) analyzes text
        ↓
Returns sentiment + urgency score + summary (JSON)
        ↓
Saved to complaints.json with timestamp
        ↓
Dashboard auto-sorts by urgency score (highest first)
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| UI Framework | Streamlit |
| AI Model | Groq API — LLaMA 3.3-70b-versatile |
| Backend Logic | Python 3.x |
| Data Storage | JSON file (complaints.json) |
| Environment | python-dotenv |
| Data Processing | Pandas |

---

## Setup Instructions

### Prerequisites
- Python 3.8 or above
- A free Groq API key from [console.groq.com](https://console.groq.com)

### Step 1 — Clone the repository

```bash
git clone https://github.com/kaviya-0202/Infinia-squad.git
cd Infinia-squad
```

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Configure environment

Create a `.env` file in the root folder:

```
GROQ_API_KEY=your_groq_api_key_here
```

To get your API key:
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for free
3. Click API Keys → Create API Key
4. Copy and paste it into `.env`

### Step 4 — Run the application

```bash
streamlit run app.py
```

Or if streamlit is not on PATH:

```bash
python -m streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## Run Instructions

### Submit a Complaint
1. Open the app and go to **Submit Complaint** in the sidebar
2. Enter your Full Name and Email
3. Describe your issue in the text area
4. Click **Submit Complaint**
5. The AI will analyze and show sentiment, urgency score, and priority level instantly

### View the Dashboard
1. Click **Support Dashboard** in the sidebar
2. See all complaints sorted by urgency — Critical issues appear first
3. Each card shows name, email, sentiment, urgency score, complaint text, and timestamp
4. Scroll down to see the summary table
5. Use the **Clear All** button to reset the complaint list

### Test with Sample Data
Run the sample data loader to populate the dashboard with 10 realistic complaints:

```bash
python data/sample_data.py
```

---

## Assumptions & Limitations

### Assumptions
- The Groq API key is valid and has available credits
- Complaints are submitted in English
- The application runs on a single machine (no multi-user concurrency handling)
- JSON file storage is sufficient for demo/hackathon purposes

### Limitations
- Storage is file-based (complaints.json) — not suitable for production scale
- No user authentication — anyone can access the dashboard
- The AI analysis depends on Groq API availability and rate limits
- No persistent database — complaints are lost if the JSON file is deleted
- Currently supports English language only

---

## Dependencies

```
streamlit
groq
python-dotenv
pandas
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## Team

**Infinia Squad — Infinite Computer Solutions**

Built for the Infinite Computer Solutions Use Case Build Program — June 2026

---

## License

This project was built for internal hackathon purposes at Infinite Computer Solutions.
