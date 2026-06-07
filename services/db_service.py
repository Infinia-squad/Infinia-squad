import json
import os
from datetime import datetime

DB_PATH = "data/complaints.json"

def init_db():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w") as f:
            json.dump([], f)

def save_complaint(complaint_data):
    init_db()
    complaints = get_all_complaints()
    complaint_data["id"] = len(complaints) + 1
    complaint_data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    complaints.append(complaint_data)
    with open(DB_PATH, "w") as f:
        json.dump(complaints, f, indent=2)
    return complaint_data

def get_all_complaints():
    init_db()
    with open(DB_PATH, "r") as f:
        return json.load(f)

def get_sorted_complaints():
    complaints = get_all_complaints()
    return sorted(complaints, key=lambda x: x.get("urgency_score", 0), reverse=True)

def clear_all_complaints():
    with open(DB_PATH, "w") as f:
        json.dump([], f)
