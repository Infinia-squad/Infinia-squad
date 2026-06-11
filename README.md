# 🚨 AI-Powered Customer Complaint Prioritization System

<div align="center">

**Built for the Infinite Computer Solutions Hackathon · June 2026**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=for-the-badge&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-LLaMA3-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

### 👥 Team Infinia Squad

| Member | Role |
|--------|------|
| Mathumitha.S | AI Integration & Scoring Engine |
| Kaviya.S | UI / Dashboard |
| Hemavarni.S | Backend Logic, Testing & Docs |

</div>

---

## 📌 Problem Statement

Customer support teams receive hundreds of tickets daily — most are routine, but some signal **angry customers on the verge of churning**, **production outages**, or **legal threats**. These critical tickets get buried in the queue and are handled too late.

> **This tool uses AI to instantly score every incoming complaint and surface the most dangerous ones — before it's too late.**

---
## 🎥 Demo Video

Watch the full end-to-end demo here:

- [🔗 Link 1: Live Demo](https://demo-video-delta.vercel.app/)
- [🔗 Link 2: Google Drive Video](https://drive.google.com/file/d/1UcjNR4Dj_JZWSEskOfXxcnNy0tk_ejCz/view?usp=sharing)
- 
## 🚀 Live App (Streamlit)

You can try the project live here:  
[Click to Open App](https://infinia-squad-endvkt6hdajyhbkhurhp2p.streamlit.app/)

## ✨ Features

- 🤖 **AI Sentiment Analysis** — Classifies tone as Positive / Neutral / Negative using LLaMA 3
- 🔥 **Urgency Scoring** — Rates each ticket 1–10 and labels it Low / Medium / High / Critical
- ⚠️ **Churn Risk Detection** — Flags language indicating a customer may leave
- 📊 **Live Support Dashboard** — Complaints sorted by urgency in real-time
- 🃏 **Color-Coded Complaint Cards** — Visual priority at a glance
- 📋 **Summary Table** — Quick overview of all complaint statuses
- 💡 **AI Reasoning** — Explains *why* a ticket was flagged, not just the score

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend & UI | Streamlit |
| AI Brain | Groq API (LLaMA 3 8B) |
| Backend | Python 3.10+ |
| Storage | JSON (flat file) |
| Testing | Pytest |
| Version Control | GitHub |

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                       USER INTERFACE                         │
│    Customer fills complaint form  →  Streamlit (user_form)  │
└──────────────────────────┬──────────────────────────────────┘
                           │  Raw complaint text
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    AI SCORING ENGINE                         │
│                   groq_service.py                           │
│                                                             │
│   Prompt sent to Groq API (LLaMA 3 8B):                    │
│     - Sentiment Score  (1–10)                               │
│     - Urgency Score    (1–10)                               │
│     - Churn Risk       (low / medium / high)                │
│     - Reason           (1-line explanation)                 │
│     - Recommended Action                                    │
└──────────────────────────┬──────────────────────────────────┘
                           │  Structured JSON response
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  THRESHOLD DECISION LAYER                    │
│                                                             │
│   IF sentiment ≥ 7  OR  urgency ≥ 8  OR  churn = high      │
│       → Mark as HIGH / CRITICAL priority                    │
│   ELSE                                                      │
│       → Mark as LOW / MEDIUM and log quietly               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    DATA STORAGE LAYER                        │
│                    db_service.py                            │
│                                                             │
│   Saves complaint + AI scores → complaints.json            │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   SUPPORT DASHBOARD                          │
│                   dashboard.py                              │
│                                                             │
│   Reads complaints.json → Renders sorted color-coded cards  │
│   Critical 🔴  →  High 🟠  →  Medium 🟡  →  Low 🟢        │
└─────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

| File | What it does |
|------|-------------|
| `app.py` | Entry point, Streamlit multi-page setup |
| `pages/user_form.py` | Customer-facing complaint submission form |
| `pages/dashboard.py` | Support team view, sorted by urgency |
| `services/groq_service.py` | Calls Groq API, parses and returns scores |
| `services/db_service.py` | Read/write complaints to JSON storage |
| `data/complaints.json` | Persisted complaint records |
| `data/sample_data.py` | Pre-loaded demo complaints for testing |
| `utils/helpers.py` | Shared formatting and threshold logic |

---

## ⚙️ Setup Instructions

### Prerequisites

- Python **3.10 or higher** — check with `python --version`
- A free [Groq API key](https://console.groq.com) (takes 2 minutes to get)

### Step 1 — Clone the Repository

```bash
git clone https://github.com/infinia-squad/complaint-prioritizer.git
cd complaint-prioritizer
```

### Step 2 — Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure Environment Variables

Create a `.env` file in the root directory:

```bash
# On macOS/Linux:
touch .env

# On Windows:
echo. > .env
```

Add your Groq API key to the `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> **Get your free key:** Go to [console.groq.com](https://console.groq.com) → Sign up → Create API Key → Paste above.

### Step 5 — Load Sample Data (Optional but Recommended for Demo)

```bash
python data/sample_data.py
```

This pre-loads 10 varied complaints (mix of low and critical) so the dashboard looks populated for the demo.

---

## ▶️ Run Instructions

### Start the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at:

```
http://localhost:8501
```

### Navigating the App

The app has **two pages** accessible from the left sidebar:

| Page | URL | Purpose |
|------|-----|---------|
| 📝 Submit Complaint | `/user_form` | Customer submits a complaint |
| 📊 Dashboard | `/dashboard` | Support team views prioritized queue |

### Typical Demo Flow

1. Open the app → go to **Submit Complaint**
2. Type or paste a complaint (try something urgent like *"Our entire payment system is down and we're losing thousands per minute"*)
3. Click **Analyze & Submit**
4. Switch to **Dashboard** in the sidebar
5. See the complaint appear at the top, color-coded **Critical 🔴**
6. Submit a low-priority complaint (*"Can you update my billing address?"*) and see it land at the bottom **Low 🟢**

### Running Tests

```bash
pytest tests/ -v
```

Expected output: all tests pass with a summary of scoring accuracy and edge case handling.

---

## 📁 Project Structure

```
complaint-prioritizer/
├── app.py                    # Main entry point
├── pages/
│   ├── user_form.py          # Customer complaint form
│   └── dashboard.py          # Support team dashboard
├── services/
│   ├── groq_service.py       # Groq AI analysis + scoring
│   └── db_service.py         # JSON data storage layer
├── data/
│   ├── complaints.json       # Stored complaints (auto-created)
│   └── sample_data.py        # Pre-loads demo complaints
├── utils/
│   └── helpers.py            # Threshold logic + formatting
├── tests/
│   ├── test_scoring.py       # Unit tests for AI scoring
│   └── test_threshold.py     # Tests for priority decision logic
├── docs/
│   └── ai_usage_note.md      # What AI helped with, best prompts
├── .env                      # API keys (do NOT commit)
├── .env.example              # Template for .env (safe to commit)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧪 Sample Data

The `data/sample_data.py` file contains 10 pre-written complaints that demonstrate the full range of scoring:

| Ticket | Expected Priority |
|--------|-----------------|
| "Our checkout is completely broken, we can't process orders" | 🔴 Critical |
| "I'm switching to your competitor if this isn't fixed today" | 🔴 Critical |
| "Been waiting 4 days for a response, this is unacceptable" | 🟠 High |
| "My invoice amount looks incorrect" | 🟡 Medium |
| "Can you update my email address on file?" | 🟢 Low |

Run `python data/sample_data.py` to load them before the demo.

---

## ⚠️ Assumptions & Limitations

### Assumptions

- All complaints are submitted in **English only**; multilingual input is not handled
- The Groq free tier API is **available and responsive** during the demo
- A **single user** operates the app at a time; concurrent submissions are not tested
- JSON file storage is **sufficient for prototype volume** (~100 complaints max)
- The thresholds (`sentiment ≥ 7`, `urgency ≥ 8`) are **manually tuned** and may need adjustment for production use
- The app is run **locally** on the demo machine; no cloud deployment is included

### Limitations

- **No persistent database** — all data lives in `complaints.json`; deleting it clears all history
- **No authentication** — anyone with the localhost URL can access the support dashboard
- **No real-time push** — the dashboard requires a manual browser refresh to show new submissions
- **AI response time** varies based on Groq API latency (typically 1–3 seconds)
- **No ticket editing** — once a complaint is submitted, it cannot be modified
- **Not load-tested** — designed for demo scale, not production traffic

---

## 🤖 AI Usage

See [`docs/ai_usage_note.md`](docs/ai_usage_note.md) for the full 1-page breakdown of:
- What AI (Claude/Groq) helped build
- Where AI got things wrong and how we corrected it
- The best prompts we discovered during development

**Key AI capability demonstrated:** LLM-as-classifier with structured JSON output — the AI doesn't just return a label, it returns scores, reasons, and recommended actions in a single call.

---

## 👥 Team Infinia Squad

Built with 🔥 in under 24 hours for the **Infinite Computer Solutions Hackathon, June 2026**.

> *"Ship fast, score high, fix live."*

---

*Made with ❤️ by Team Infinia Squad*
