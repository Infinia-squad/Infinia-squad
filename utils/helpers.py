def get_urgency_color(urgency_label):
    colors = {
        "Critical": "#ff4444",
        "High":     "#ff8800",
        "Medium":   "#ffcc00",
        "Low":      "#44cc44",
    }
    return colors.get(urgency_label, "#888888")

def get_sentiment_color(sentiment):
    colors = {
        "Positive": "#44cc44",
        "Neutral":  "#ffcc00",
        "Negative": "#ff4444",
    }
    return colors.get(sentiment, "#888888")

def get_urgency_emoji(urgency_label):
    emojis = {
        "Critical": "🔴",
        "High":     "🟠",
        "Medium":   "🟡",
        "Low":      "🟢",
    }
    return emojis.get(urgency_label, "⚪")

def get_sentiment_emoji(sentiment):
    emojis = {
        "Positive": "😊",
        "Neutral":  "😐",
        "Negative": "😡",
    }
    return emojis.get(sentiment, "😐")
