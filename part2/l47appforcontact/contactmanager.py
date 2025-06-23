import json
import os
class ContactManager:
     def __init__(self,jsonfileurl='contacts.json'):
          self.jsonfileurl = jsonfileurl
     def loadcontacts(self):
          if not os.path.exists(self.jsonfileurl):
               return []
          with open(self.jsonfileurl,'r') as file:
               return json.load(file)

     def savecontact(self,excontacts):
          with open(self.jsonfileurl,'w') as file:
               json.dump(excontacts,file,indent=4)

     def createcontact(self,name,phone,email):
          existingcontacts = self.loadcontacts()
          newcontact = {
               "id": len(existingcontacts) + 1,
               "name": name,
               "phone": phone,
               "email": email
          }
          existingcontacts.append(newcontact)
          self.savecontact(existingcontacts)
          print("New contact created successfully.")

     def readcontact(self):
          existingcontacts = self.loadcontacts()
          for contact in existingcontacts:
               print(f"{contact['id']}. {contact['name']}. {contact['phone']}. {contact['email']} ")

     def updatecontact(self,contactid,name=None,phone=None,email=None):
          contacts = self.loadcontacts()
          found = False
          for contact in contacts:
               if contact["id"] == contactid:
                    # if name: 
                    #      contact["name"] = name
                    # if phone: 
                    #      contact["phone"] = phone
                    # if email: 
                    #      contact["email"] = email

                    # if name: contact["name"] = name
                    # if phone: contact["phone"] = phone
                    # if email: contact["email"] = email

                    if name is not None: 
                         contact["name"] = name
                    if phone is not None: 
                         contact["phone"] = phone
                    if email is not None: 
                         contact["email"] = email

                    self.savecontact(contacts)
                    print("Contact Updated Successfully.")
                    found = True
                    return # break
          
          if not found:
               print("Contact Not Found.")


     def deletecontact(self,contactid):
          contacts = self.loadcontacts()
          newcontacts = [x for x in contacts if x["id"] != contactid]

          if len(contacts) == len(newcontacts):
               print("Contact Not Found.")
          else:
               self.savecontact(newcontacts)
               print("Contact Deleted Successfully")

     def importcontacts(self,impjsonfile):
          contacts = self.loadcontacts()
          with open(impjsonfile,'r') as file:
               imported = json.load(file)
                    
          lastid = contacts[-1]['id'] if contacts else 0

          for key,value in enumerate(imported):
               value["id"] = lastid + key + 1
               contacts.append(value)

          self.savecontact(contacts)
          print(f"Imported {len(imported)} Contacts.")

     def exportcontacts(self,expfilename):
          existingcontacts = self.loadcontacts()
          with open(expfilename,'w') as file:
                    json.dump(existingcontacts,file,indent=4)

          print(f"Exported to {expfilename}.")


# [
#      {
#           "id":1,
#      }
# ]

# new.json
# [
#      {
#           "name":"yu yu",
#           "phone":"012345",
#           "email":"yuyu@gmail.com",
#      },
#      {
#           "name":"yu yu",
#           "phone":"012345",
#           "email":"yuyu@gmail.com",
#      }
# ]