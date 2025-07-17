import firebase_admin
from firebase_admin import credentials, firestore,db

# Make sure you've already initialized Firebase here

def clear_user_list(username, list_type):
    """
    Clears the specified list (watched or to_watch) for the given user.
    """
    ref = db.reference(f'users/{username}/{list_type}')
    ref.set([])  # Reset the list to an empty array

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
def add_to_list(user_id, list_type, movie_id):
    user_ref = db.collection("users").document(user_id)
    user_ref.set({list_type: firestore.ArrayUnion([movie_id])}, merge=True)

# Get movie list for a user (watched or to_watch)
def get_user_list(user_id, list_type):
    doc = db.collection("users").document(user_id).get()
    if doc.exists:
        return doc.to_dict().get(list_type, [])
    return []