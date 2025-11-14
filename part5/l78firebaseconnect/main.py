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

     data = {
          "username": "aung aung",
          "email": "aungaung@gmail.com",
          # "createdAt": datetime.now()
          "createdAt": firestore.SERVER_TIMESTAMP # use firestore servr tmestamp
     }

     # Create Document
     # doc_ref = db.collection(collection_name).document() #  doc_ref = db.collection(collection_name).document() # = mean auto-generate ID
     # doc_ref.set(data)

     #Method 2, Push a new document with auto-generated ID
     doc_ref = db.collection(collection_name).add(data)

     print(f"Collection {collection_name} is ready in Firestore!")
except Exception as e:
     print("Error: ",e)


