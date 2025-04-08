from fastapi import FastAPI, Depends
from pydantic import BaseModel
from auth import get_current_user
from firebase import save_message, get_messages, get_documents

app = FastAPI()

class Message(BaseModel):
    conversation_id: str
    content: str

@app.post("/send/")
def send_message(msg: Message, user=Depends(get_current_user)):
    save_message(msg.conversation_id, user["sub"], msg.content)
    return {"status": "sent"}

@app.get("/messages/{conversation_id}")
def fetch_messages(conversation_id: str, user=Depends(get_current_user)):
    messages = get_messages(conversation_id)
    return {"messages": messages}

@app.get("/collections/{collection_name}")
def fetch_documents(collection_name: str, user=Depends(get_current_user)):
    documents = get_documents(collection_name)
    return {"documents": documents}