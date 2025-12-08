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

     # # FETCH ALL 
     # docs = col_ref.order_by('createdAt').stream()
     # print("\nFetch all documents\n")
     # for doc in docs:
     #      data = doc.to_dict()
     #      print(f"ID: {doc.id}, Name: {data.get('username')}, Email: {data.get('email')}, Created: {data.get('createdAt')}")

     # # FETCH SOME 
     # docs = col_ref.order_by('createdAt').limit(2).stream()
     # print("\nFetch all documents\n")
     # for doc in docs:
     #      data = doc.to_dict()
     #      print(f"ID: {doc.id}, Name: {data.get('username')}, Email: {data.get('email')}, Created: {data.get('createdAt')}")


    # FETCH SOME 
     # docs = col_ref.order_by('createdAt').limit(2).stream()
     # print("\nFetch some documents\n")
     # for doc in docs:
     #      data = doc.to_dict()
     #      print(f"ID: {doc.id}, Name: {data.get('username')}, Email: {data.get('email')}, Created: {data.get('createdAt')}")


     #     FETCH ONE 
     doc = col_ref.order_by('createdAt').limit(1).get()
     # print(doc)
     print("\nFetch one documents\n")

     if doc: 
          data = doc[0].to_dict()
          print(f"ID: {doc[0].id}, Name: {data.get('username')}, Email: {data.get('email')}, Created: {data.get('createdAt')}")

except Exception as e:
     print("Error: ",e)


# 🔥 Firestore .stream() vs .get() — Easy Explanation
# ✅ 1. .stream()
# What it does

# Returns a generator (lazy iterator).

# Documents are fetched one-by-one as you loop.

# Does not load all documents into memory at once.

# Good for large collections.

# Usage
# docs = col_ref.order_by('createdAt').limit(2).stream()
# for doc in docs:
#     print(doc.id)

# Characteristics
# Feature	.stream()
# Fetch style	Lazy (one at a time)
# Memory	Low (not all data loaded)
# Returns	Generator of DocumentSnapshot
# When data downloads	Only when looping
# ✅ 2. .get()
# What it does

# Returns a list of documents immediately.

# All matched documents are downloaded at once.

# Good when the dataset is small or you need indexed access (doc[0]).

# Usage
# doc_list = col_ref.order_by('createdAt').limit(1).get()

# Characteristics
# Feature	.get()
# Fetch style	Fetch all at once
# Memory	Higher (list of docs)
# Returns	List of DocumentSnapshot
# When data downloads	Immediately when called



# *result
# -------------------------------
# stream()
# $ py main.py
# <google.cloud.firestore_v1.stream_generator.StreamGenerator object at 0x00000241C6699760>

# Fetch all documents

# ID: text_dockey, Name: aung aung, Email: aungaung@gmail.com, Created: 2025-11-14 14:43:36.543000+00:00
# ID: Gpy4HinRW4Qkaue1lUxx, Name: aung aung, Email: aungaung@gmail.com, Created: 2025-11-14 14:58:39.277000+00:00

# =>get()
# $ py main.py
# [<google.cloud.firestore_v1.base_document.DocumentSnapshot object at 0x00000133A0B25460>, <google.cloud.firestore_v1.base_document.DocumentSnapshot object at 0x00000133A2BD1280>]

# Fetch one documents

# {'username': 'aung aung', 'createdAt': DatetimeWithNanoseconds(2025, 11, 14, 14, 43, 36, 543000, tzinfo=datetime.timezone.utc), 'email': 'aungaung@gmail.com'}
# (myenv)
