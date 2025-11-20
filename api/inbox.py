from fastapi import APIRouter
from db.mongodb import notifications_col, emails_col

router = APIRouter()

@router.get("/all")
async def unified_inbox():
    notifications = list(notifications_col.find().sort("time", -1))
    emails = list(emails_col.find().sort("time", -1))

    return {
        "notifications": notifications,
        "emails": emails
    }
