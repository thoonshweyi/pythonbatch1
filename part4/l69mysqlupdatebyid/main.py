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


update_sql = 'UPDATE staffs SET username=%s, email=%s WHERE id=%s'

# Connect to server

try:
     conn = mysql.connector.connect(**config)
     if(conn.is_connected()):
          # Get a cursor
          cursor = conn.cursor()

          try:
               userid = input("Enter ID to search: ")
               newname = input("Enter new name: ")
               newemail = input("Enter new email: ")
 
               cursor.execute(update_sql,(newname,newemail,userid)) #  

               conn.commit()
               if cursor.rowcount > 0:
                    print("Record updated successfully")
               else:
                    print("No record found with that ID")

          finally:
               cursor.close() # Close cursor
               conn.close() # Close connection

except Error as e:
     print("Error",e)



