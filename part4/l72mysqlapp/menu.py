from staff import Staff
class AppMenu:
     def __init__(self):
          self.staff = Staff()

     def display(self):
          while True:
               print("\n ==== Menu ===")
               print("1. Create Staff")
               print("2. Read All Staff")
               print("3. Update Staff")
               print("4. Delete Staff")
               print("5. Exit")

               choice = input("Enter choice (1-5): ")

               if choice == "1":
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    self.staff.create(name,email)
               elif choice == "2":
                    self.staff.readall()
               elif choice == "3":
                    userid = input("Enter ID to update: ")
                    newname = input("Enter new name: ")
                    newemail = input("Enter new email: ")
                    
                    self.staff.update(userid,newname,newemail)
               elif choice == "4":
                    userid = input("Enter ID to delete: ")
                    confirm = input("Are you sure? (y/n): ").lower()

                    if(confirm == "y"):
                         self.staff.delete(userid)
                    else:
                         print("Delete cancelled.")
               elif choice == "5":
                    print("Existing program. Goodbye!")
                    break
               else:
                    print("Invalid choice, try again")
