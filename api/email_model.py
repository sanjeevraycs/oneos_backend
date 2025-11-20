from pydantic import BaseModel

class EmailModel(BaseModel):
    sender: str
    subject: str
    message: str
    timestamp: str | None = None
    category: str | None = "general"
