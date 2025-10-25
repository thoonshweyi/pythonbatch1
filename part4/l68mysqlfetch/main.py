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


selectall_sql = 'SELECT id,username,email,created_at FROM staffs ORDER BY id'


# Connect to server

try:
     conn = mysql.connector.connect(**config)
     if(conn.is_connected()):
          # Get a cursor
          cursor = conn.cursor()

          try:
               # => Method 1 Execute a query fetchone()
               # cursor.execute(selectall_sql)
               # row = cursor.fetchone()
               # # print(row) # (1, 'aung aung', 'aungaung@gmail.com', datetime.datetime(2025, 10, 21, 22, 42, 6)) Error Unread result found
               # while row is not None:
               #      print(row)
               #      row = cursor.fetchone()

               # => Method 2 Execute a query fetchall()
               cursor.execute(selectall_sql)
               rows = cursor.fetchall()
               # print(rows)
               for row in rows:
                    # print(row)

                    print(f"ID: {row[0]} . Name {row[1]}. Email {row[2]} . Created At {row[3]}")

               # => Method 3 Execute a query fetchmany(size)
               # cursor.execute(selectall_sql)
               # rows = cursor.fetchmany(2)
               # for row in rows:
               #      print(row)
               #      rows = cursor.fetchmany(2)

          finally:
               cursor.close() # Close cursor
               conn.close() # Close connection

except Error as e:
     print("Error",e)



