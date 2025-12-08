import firebase_admin
from firebase_admin import credentials,firestore
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv() 
try:
     # cred = credentials.Certificate('./serviceAccountKey.json')
     cred = credentials.Certificate({
          "type": os.getenv("FIREBASE_TYPE"),
          "project_id": os.getenv("FIREBASE_PROJECT_ID"),
          "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
          "private_key": os.getenv("FIREBASE_PRIVATE_KEY"),
          "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
          "client_id": os.getenv("FIREBASE_CLIENT_ID"),
          "auth_uri": os.getenv("FIREBASE_AUTH_URL"),
          "token_uri": os.getenv("FIREBASE_TOKEN_URL"),
          "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_CENT_URL"),
          "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_CERT_URL"),
          "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN"),
     })

     app = firebase_admin.initialize_app(cred)

     # Get firebase client 
     db = firestore.client()

     # Collection
     collection_name="employees"

     col_ref = db.collection(collection_name)

     # Input document ID (string)
     doc_id = input("Enter ID to search: ")

     # Get document reference
     doc_ref = col_ref.document(doc_id)

     # GET document by ID
     doc = doc_ref.get()

     if doc.exists:
          doc_ref.delete()
          print("Record deleted successfully")
     else:
          print(f"No record found with that ID.")


except Exception as e:
     print("Error: ",e)


# ✅ What is a Firestore batch?

# A batch is a special feature in Firestore that lets you send multiple operations (writes) to Firestore in one single request.

# This means instead of:

# Making many network requests

# Writing documents one by one

# You group all operations together and send them at once.

# 🧑‍🏫 Analogy:

# Imagine you want to send 50 letters.

# Without batch:
# You go to the post office 50 times → slow.

# With batch:
# You collect all letters in one bag and send them in one trip → fast.

# That bag is the batch.

# 🔥 What batch can do

# Batch can include:

# Operation	Meaning
# batch.set()	Create or overwrite a document
# batch.update()	Update existing fields
# batch.delete()	Delete a document

# Batch can contain up to 500 operations.