from fastapi import APIRouter
from db.mongodb import users_col

router = APIRouter()

@router.post("/create")
async def create_user(payload: dict):
    users_col.insert_one(payload)
    return {"status": "user_created"}
