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


insert_sql = "INSERT INTO staffs(username,email) VALUES (%s,%s)"
values_sql = [
     # ('su su','susu@gmail.com'),
     # ('nu nu','nunu@gmail.com'),
     # ('yu yu','yuyu@gmail.com')
     
     ('tun tun','tuntun@gmail.com')
]




# Connect to server

try:
     conn = mysql.connector.connect(**config)
     if(conn.is_connected()):
          # Get a cursor
          cursor = conn.cursor()

          try:
               # Execute a query
               cursor.executemany(insert_sql,values_sql)
               conn.commit()
               print("Data Inserted, rows are = ", cursor.rowcount)
               print("Data Inserted, id is = ", cursor.lastrowid)
          finally:
               cursor.close() # Close cursor
               conn.close() # Close connection

except Error as e:
     print("Error",e)



