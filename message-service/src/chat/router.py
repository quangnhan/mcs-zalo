from fastapi import APIRouter, HTTPException
from typing import List
from src.chat import service
from .schemas import MessageOut, MessageCreate

router = APIRouter(tags=["Messages"])

@router.post("/{conversation_id}", response_model=dict)
def send_message(conversation_id: str, message: MessageCreate):
    try:
        message_id = service.save_message(
            conversation_id=conversation_id,
            sender_id=message.sender_id,
            content=message.content
        )
        return {"message_id": message_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.get("/{conversation_id}")
@router.get("/{conversation_id}", response_model=List[MessageOut])
def fetch_messages(conversation_id: str, limit: int = 50):
    try:
        return service.get_messages(conversation_id, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/collections/", response_model=List[str])
def fetch_collections():
    try:
        return service.get_collections()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/collections/{collection_name}/", response_model=List[dict])
def fetch_collection(collection_name: str):
    try:
        return service.get_collection(collection_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
