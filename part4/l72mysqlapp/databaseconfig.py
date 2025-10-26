import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
     def __init__(self):
          self.config = {
               "host": os.getenv("DB_HOST"),
               "port": os.getenv("DB_PORT"),
               "user": os.getenv("DB_USER"),
               "password": os.getenv("DB_PASS"),
               "database": os.getenv("DB_NAME")
          }

          self.conn = None
          self.cursor = None

     def connect(self):
          try:
               self.conn = mysql.connector.connect(**self.config)
               self.cursor = self.conn.cursor()
          except Error as e:
               print("Error while connecting to database: ",e)

     def close(self):
          if self.cursor:
               self.cursor.close()
          if self.conn:
               self.conn.close()


