from contactmanager import ContactManager;
def main():
     contactObj = ContactManager()
     while True:
          print("\n Contact Manager App")
          print("1. Create Contact")
          print("2. Read Contact")
          print("3. Update Contact")
          print("4. Delete Contact")
          print("5. Import Contact")
          print("6  Export Contact")
          print("7. exit")

          choice = input("Choose an option: ")
          if choice == "1":
               name = input("Name: ")
               phone = input("Phone: ")
               email = input("Email: ")
               contactObj.createcontact(name,phone,email)
          elif choice == "2":
               contactObj.readcontact()

          elif choice == "3":
               contactid = int(input("Contact ID to edit: "))
               name = input("New name (blank to skip)")
               phone = input("New phone (blank to skip)")
               email = input("New email (blank to skip)")
               contactObj.updatecontact(contactid,name or None, phone or None, email or None)

          elif choice == "4":
               contactid = int(input("Contact ID to edit: "))
               contactObj.deletecontact(contactid)
          elif choice == "5":
               impjsonfile = input("Import file (JSON): ")
               contactObj.importcontacts(impjsonfile)
          elif choice == "6":
               expjsonfile = input("Export file (JSON): ")
               contactObj.exportcontacts(expjsonfile)
          elif choice == "7":
               print("Goodbye !")
               break
          else:
               print("Invalid Choice.")

          
if __name__ == "__main__":
     main()


# ---- Contact Manager ----
# 1. Create Contact (i) Name (ii) Phone (iii) Email
# 2. Read Contacts
# 3. Update Contact
# 4. Delete Contact
# 5. Import Contact
# 6. Export Contact
# 7. exit (auto save(json))