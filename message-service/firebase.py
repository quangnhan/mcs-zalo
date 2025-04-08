import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv
load_dotenv()

if not firebase_admin._apps:
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()

def save_message(conversation_id: str, sender_id: str, content: str):
    ref = db.collection("conversations").document(conversation_id).collection("messages")
    return ref.add({
        "sender": sender_id,
        "content": content,
        "timestamp": firestore.SERVER_TIMESTAMP
    })

def get_messages(conversation_id: str, limit: int = 50):
    ref = db.collection("conversations").document(conversation_id).collection("messages")
    docs = ref.order_by("timestamp", direction=firestore.Query.DESCENDING).limit(limit).stream()
    return [doc.to_dict() for doc in docs]

def get_documents(collection_name: str):
    docs = db.collection(collection_name).stream()
    return [doc.to_dict() for doc in docs]