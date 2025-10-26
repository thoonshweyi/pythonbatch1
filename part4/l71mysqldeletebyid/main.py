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


delete_sql = 'DELETE FROM staffs WHERE id=%s'

# Connect to server

try:
     conn = mysql.connector.connect(**config)
     if(conn.is_connected()):
          # Get a cursor
          cursor = conn.cursor()

          try:
               userid = input("Enter ID to delete: ")
             
 
               cursor.execute(delete_sql,(userid,)) # *****
               conn.commit()

               if cursor.rowcount > 0:
                    print("Record deleted successfully")
               else:
                    print("No record found with that ID")

          finally:
               cursor.close() # Close cursor
               conn.close() # Close connection

except Error as e:
     print("Error",e)



