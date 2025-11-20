from fastapi import APIRouter
from utils.summarize import summarize

router = APIRouter()

@router.post("/chat")
async def ai_chat(payload: dict):
    text = payload.get("text")
    result = summarize(text)
    return {"reply": result}
