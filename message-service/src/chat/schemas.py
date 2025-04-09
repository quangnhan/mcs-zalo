from pydantic import BaseModel

class MessageCreate(BaseModel):
    sender_id: str
    content: str

class MessageOut(BaseModel):
    sender: str
    content: str
    timestamp: str