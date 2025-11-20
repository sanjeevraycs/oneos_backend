from fastapi import APIRouter
from db.mongodb import notifications_col
from utils.classifier import classify

router = APIRouter()

@router.post("/ingest")
async def ingest_notification(payload: dict):
    # Add AI classification
    importance = classify(payload.get("content", ""))

    data = {
        "title": payload.get("title"),
        "content": payload.get("content"),
        "app": payload.get("app"),
        "time": payload.get("time"),
        "importance": importance
    }

    notifications_col.insert_one(data)

    return {"status": "stored", "importance": importance}
