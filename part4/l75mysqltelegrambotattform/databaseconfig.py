import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

config = {
     "host": os.getenv("DB_HOST"),
     "port": os.getenv("DB_PORT"),
     "user": os.getenv("DB_USER"),
     "password": os.getenv("DB_PASS"),
     "database": os.getenv("DB_NAME")
}


def dbconnect():
     return mysql.connector.connect(**config)