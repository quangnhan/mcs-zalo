from google.cloud import firestore
from typing import List, Dict
from .config import db

class FirestoreClient:
    def __init__(self):
        self.db = db

    def get_collections(self) -> List[str]:
        """
        List all top-level collection names in the Firestore database.

        Returns:
            List[str]: A list of collection names (e.g., ["users", "orders"]).
        """
        return [collection.id for collection in self.db.collections()]

    def get_collection(self, collection_name: str) -> List[Dict]:
        """
        Retrieve all documents from a specific collection.

        Args:
            collection_name (str): The name of the Firestore collection.

        Returns:
            List[Dict]: A list of documents, where each document is a dictionary
                        representing the document's fields and values.
        """
        collection_ref = self.db.collection(collection_name)
        return [doc.to_dict() for doc in collection_ref.stream()]

    def get_collection_ref(self, collection_name: str) -> firestore.CollectionReference:
        """
        Get a reference to a specific collection.

        Args:
            collection_name (str): The name of the Firestore collection.

        Returns:
            CollectionReference: A reference to the specified collection.
        """
        return self.db.collection(collection_name)