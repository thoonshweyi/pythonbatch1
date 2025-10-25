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


select_sql = 'SELECT * FROM staffs WHERE id = %s'


# Connect to server

try:
     conn = mysql.connector.connect(**config)
     if(conn.is_connected()):
          # Get a cursor
          cursor = conn.cursor()

          try:
               userid = input("Enter ID to search: ")
               cursor.execute(select_sql,(userid,)) # Error Could not process parameters: str(4), it must be of type list, tuple or dict

               row = cursor.fetchone()
            
               if row:
                    print("Record Found: ",row)
               else:
                    print("No Record Found with that ID.")

          finally:
               cursor.close() # Close cursor
               conn.close() # Close connection

except Error as e:
     print("Error",e)



