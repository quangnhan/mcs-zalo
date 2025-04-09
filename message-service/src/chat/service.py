from typing import List
from src.firebase.client import FirestoreClient
from firebase_admin import firestore
from .schemas import MessageOut

client = FirestoreClient()

def save_message(conversation_id: str, sender_id: str, content: str):
    ref = client.get_collection_ref(conversation_id)
    _, doc_ref = ref.add({
        "sender": sender_id,
        "content": content,
        "timestamp": firestore.SERVER_TIMESTAMP
    })
    
    return doc_ref.id

def get_messages(conversation_id: str, limit: int = 50) -> List[MessageOut]:
    ref = client.get_collection_ref(conversation_id)
    docs = ref.order_by("timestamp", direction=firestore.Query.DESCENDING).limit(limit).stream()

    result = []
    for doc in docs:
        data = doc.to_dict()
        if "timestamp" in data and data["timestamp"] is not None:
            result.append(MessageOut(
                sender=data["sender"],
                content=data["content"],
                timestamp=data["timestamp"].isoformat()
            ))
    return result

def get_collections():
    collections = client.get_collections()
    return collections

def get_collection(collection_name: str):
    ref = client.get_collection(collection_name)
    print("Collection Reference:", ref)
    return ref
