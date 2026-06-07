import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

def analyze_complaint(complaint_text):
    api_key = os.environ.get("GROQ_API_KEY")
    
    if not api_key or api_key == "your_groq_api_key_here":
        return {
            "sentiment": "Neutral",
            "sentiment_symbol": "~",
            "urgency_score": 5,
            "urgency_label": "Medium",
            "summary": "API key not configured",
            "error": "No API key found"
        }

    client = Groq(api_key=api_key)

    prompt = f"""
You are a customer support AI assistant. Analyze the following customer complaint and return ONLY a JSON object with no extra text, no markdown, no explanation.

Complaint: "{complaint_text}"

Return exactly this JSON format:
{{
    "sentiment": "Positive" or "Neutral" or "Negative",
    "sentiment_symbol": "+" or "~" or "-",
    "urgency_score": <integer from 1 to 10>,
    "urgency_label": "Low" or "Medium" or "High" or "Critical",
    "summary": "<one line summary of the complaint>"
}}
"""

    try:
        response = client.chat.completions.create(
          model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=200,
        )

        raw = response.choices[0].message.content.strip()
        
        # Strip markdown code blocks if present
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        
        result = json.loads(raw.strip())
        return result

    except Exception as e:
        return {
            "sentiment": "Neutral",
            "sentiment_symbol": "~",
            "urgency_score": 5,
            "urgency_label": "Medium",
            "summary": f"Error: {str(e)}",
        }