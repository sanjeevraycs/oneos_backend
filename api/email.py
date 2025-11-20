from fastapi import APIRouter, HTTPException
from api.email_model import EmailModel
from db.mongodb import emails_col
from utils.classifier import classify
from api.email_model import EmailModel

router = APIRouter()

@router.post("/save")
async def save_email(email: EmailModel):
    # Prevent duplicates by same sender + subject + timestamp
    exists = emails_col.find_one({
        "sender": email.sender,
        "subject": email.subject,
        "timestamp": email.timestamp
    })

    if exists:
        return {"status": "exists", "message": "Email already saved"}

    # Classify email importance
    email_type = classify(email.subject + " " + email.body)

    data = {
        "sender": email.sender,
        "subject": email.subject,
        "body": email.body,
        "timestamp": email.timestamp,
        "type": email_type,
        "unread": True
    }

    emails_col.insert_one(data)

    return {"status": "saved", "type": email_type}
