from fastapi import FastAPI
from api import notifications, inbox, ai, user, email

app = FastAPI(
    title="ONEOS Backend",
    description="Backend for unified inbox + AI",
    version="1.0.0"
)

app.include_router(notifications.router, prefix="/notifications")
app.include_router(inbox.router, prefix="/inbox")
app.include_router(ai.router, prefix="/ai")
app.include_router(user.router, prefix="/user")
app.include_router(email.router, prefix="/email")

@app.get("/")
def root():
    return {"message": "ONEOS Backend Running"}
