def classify(text):
    text = text.lower()

    if any(x in text for x in ["urgent", "immediately", "asap"]):
        return "urgent"

    if any(x in text for x in ["meeting", "call", "schedule", "event"]):
        return "meeting"

    if any(x in text for x in ["otp", "transaction", "bank", "payment"]):
        return "finance"

    if any(x in text for x in ["assignment", "exam", "class"]):
        return "education"

    if any(x in text for x in ["delivery", "order", "package"]):
        return "shopping"

    return "general"
