import firebase_admin
from firebase_admin import credentials, firestore
from src.config import settings

if not firebase_admin._apps:
    cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)

# Export Firestore client
db = firestore.client()
