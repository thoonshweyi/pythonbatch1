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

createtable_sql = '''
     CREATE TABLE IF NOT EXISTS staffs(
          id INT AUTO_INCREMENT PRIMARY KEY,
          username VARCHAR(50) NOT NULL,
          email VARCHAR(100) UNIQUE NOT NULL,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     ) ENGINE=InnoDB;
'''


# Connect to server

try:
     conn = mysql.connector.connect(**config)
     if(conn.is_connected()):
          # Get a cursor
          cursor = conn.cursor()

          # Execute a query
          cursor.execute(createtable_sql)
          conn.commit()
          print("Table created successfully!")

          cursor.close() # Close cursor
          conn.close() # Close connection
     
except Error as e:
     print("Error",e)



