import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore,db
import json

# Load Firebase credentials from Streamlit Secrets
if not firebase_admin._apps:
    firebase_cert = json.loads(st.secrets["FIREBASE_KEY"])
    cred = credentials.Certificate(firebase_cert)
    firebase_admin.initialize_app(cred)

# Firestore DB instance
db = firestore.client()

def add_to_list(user_id, movie):
    doc_ref = db.collection("user_lists").document(user_id)
    doc_ref.set({"movies": firestore.ArrayUnion([movie])}, merge=True)

def get_user_list(user_id):
    doc_ref = db.collection("user_lists").document(user_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict().get("movies", [])
    return []

def clear_user_list(username, list_type):
    """
    Clears the specified list (watched or to_watch) for the given user.
    """
    ref = db.reference(f'users/{username}/{list_type}')
    ref.set([])  # Reset the list to an empty array
