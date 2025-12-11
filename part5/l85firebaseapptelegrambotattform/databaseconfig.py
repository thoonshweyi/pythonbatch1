import firebase_admin
from firebase_admin import credentials,firestore
from datetime import datetime
from dotenv import load_dotenv
import os



load_dotenv() 
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

if not firebase_admin._apps:
     firebase_admin.initialize_app(cred)

# Get firebase client 
db = firestore.client()

def dbconnect():
     return db
