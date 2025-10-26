from databaseconfig import Database
from mysql.connector import Error

class Staff(Database):
     def create(self,name,email):
          try:
               self.connect()
               insert_sql = "INSERT INTO staffs (username,email) VALUE (%s,%s)"
               self.cursor.execute(insert_sql,(name,email))
               self.conn.commit()

               print(f"Data Inserted, ID is = : {self.cursor.lastrowid}")
          except Error as e:
               print("Error during insert:",e)
          finally:
               self.close()
     
     def readall(self):
          try:
               self.connect()
               selectall_sql = "SELECT * FROM staffs"
               self.cursor.execute(selectall_sql)
               rows = self.cursor.fetchall()
               if rows:
                    print("\n Staff List: ")
                    for row in rows:
                         print(f"ID: {row[0]}, Name: {row[2]}, Email: {row[2]}, Created: {row[3]}")
               else:
                    print(f"No staffs found!")

          except Error as e:
               print("Error during read all:",e)
          finally:
               self.close()
     
     def update(self,userid,name,email):
          try:
               self.connect()
               update_sql = "UPDATE staffs SET username=%s, email=%s WHERE id=%s"
               self.cursor.execute(update_sql,(name,email,userid))
               self.conn.commit()

               if self.cursor.rowcount > 0:
                    print(f"Staff updated successfully.")
               else:
                    print(f"No staff found with that ID")
          except Error as e:
               print("Error during update:",e)
          finally:
               self.close()
     
     def delete(self,userid):
          try:
               self.connect()
               delete_sql = "DELETE FROM staffs WHERE id=%s"
               self.cursor.execute(delete_sql,(userid,))
               self.conn.commit()

               if self.cursor.rowcount > 0:
                    print(f"Staff deleted successfully.")
               else:
                    print(f"No staff found with that ID")
          except Error as e:
               print("Error during delete:",e)
          finally:
               self.close()
