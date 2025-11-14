import firebase_admin
from firebase_admin import credentials,firestore
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
     collection_name="testcollections"

     # Create Document
     doc_ref = db.collection(collection_name).document("text_dockey") #  doc_ref = db.collection(collection_name).document() # = mean auto-generate ID
     doc_ref.set({"message":"Connected"})

     # Read the document 
     doc = doc_ref.get()
     if doc.exists:
          print(f"Firestore connected succesfully: {doc.to_dict()}")
     else:
          print("Fire connected failed!")
except Exception as e:
     print("Error: ",e)



# ✅ 1. Firebase Admin SDK
# ✔ What it is

# The Firebase Admin SDK is a backend/server library that gives your server full access to Firebase services such as:

# Firestore

# Firebase Authentication

# Firebase Cloud Messaging (FCM)

# Storage

# Realtime Database

# ✔ Why it exists

# Firebase normally has a Client SDK (for apps & websites), but this Client SDK is limited by security rules.

# Example:
# Your mobile app cannot delete all users — it's unsafe.

# So Google created the Admin SDK, which has admin privileges. It is used in:

# Backend servers (Node.js, Python, PHP, Java)

# Cloud Functions

# CRON jobs

# Admin dashboards

# Migration scripts

# ✔ What makes it powerful?

# Because Admin SDK uses a service account, it can:

# Bypass Firestore security rules

# Read/Write any document

# Manage all users

# Send push notifications

# Upload/delete files

# Access everything with no restrictions

# ✔ Example
# import firebase_admin
# from firebase_admin import credentials, firestore


# Just importing this is using the Admin SDK.

# ✅ 2. initialize_app()
# ✔ What it does

# initialize_app() is the function that activates the Firebase Admin SDK.

# You must provide service account credentials:

# cred = credentials.Certificate("serviceAccount.json")
# app = firebase_admin.initialize_app(cred)

# ✔ Why you must initialize

# Your server needs to "log in" to Firebase before accessing Firestore or Authentication.

# initialize_app() does this login using:

# project_id

# private_key_id

# private_key

# client_email

# All of these come from your Firebase service account JSON.

# ✔ What happens internally

# Reads service account JSON

# Authenticates to Google Cloud

# Generates backend tokens

# Unlocks admin-level access to Firestore, FCM, Auth, etc.

# ✔ Without initialize_app()

# Nothing works.
# Firestore cannot connect.
# Authentication fails.

# ✅ 3. Firestore Client (firestore.client())
# ✔ What it is

# This is the database driver used to communicate with Firestore.

# After Admin initializes, you create a Firestore client:

# db = firestore.client()


# Think of it like:

# Admin SDK = the whole Firebase system

# Firestore client = the part that talks to the Firestore database

# ✔ What the Firestore client allows you to do
# ✔ Create collections
# db.collection("users")

# ✔ Create new documents
# db.collection("users").document("1001").set({"name": "John"})

# ✔ Read documents
# doc = db.collection("users").document("1001").get()
# print(doc.to_dict())

# ✔ Query documents
# db.collection("users").where("age", ">", 20).get()

# ✔ Delete documents
# db.collection("users").document("1001").delete()

# ✔ Why you need a client

# Firestore is a separate Google service.
# The client is your “connection object” to send commands.

# Just like:

# SQL needs a DB connection

# MongoDB needs a client

# Firestore needs a Firestore client

# 🔥 Simple Real-World Analogy
# Thing	Real-World Example
# Firebase Admin SDK	The whole office building access system
# initialize_app()	Your access card to enter the building
# Firestore Client	The specific office room key for Firestore
# 🔍 Full Summary
# Thing	Meaning	What It Does	When You Use It
# Firebase Admin SDK	Backend library with full privileges	Gives unlimited control of Firebase	Always
# initialize_app(cred)	Login using service account	Authenticates your server	At program start
# firestore.client()	Database connection	Read/Write Firestore documents	Every Firestore operation