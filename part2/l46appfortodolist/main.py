from task import TaskJob

taskjobObj = TaskJob()

def main():
     filename = "tasks.json"
     taskjobObj.loadfile(filename)

     def menu():
          print("\n---- Task Menu ----")
          print("1. Add New Task")
          print("2. List Tasks")
          print("3. Set Complete Task")
          print("4. Delete Task")
          print("5. Tasks Report")
          print("6. Save Tasks")
          print("7. exit \n")

     def getpriority():
          try:
               return int(input("Enter priority (1 to 5): "))
          except ValueError:
               print("Invalid Input, setting priority to default 1.")
               return 1
               

     while True:
          menu()
          getnum = input("Choice number: ")
          if getnum == "1":
               title = input("Enter task title: ")
               priority = getpriority()
               taskjobObj.addnewtask(title,priority) 
          elif getnum == "2":
               taskjobObj.listtasks()
          elif getnum == "3":
               taskjobObj.listtasks()
               getindex = int(input("Enter task number to completed: "))
               taskjobObj.setcompletask(getindex)
          elif getnum == "4":
               taskjobObj.listtasks()
               getindex = int(input("Enter task number to delete: ")) 
               taskjobObj.deletetask(getindex)
          elif getnum == "5":
               taskjobObj.taskreport()
          elif getnum == "6":
               taskjobObj.savetasks(filename)
          elif getnum == "7":
               taskjobObj.savetasks(filename)
               print("Thank You")
               break
          else:
               print('Invalid Choice!')

if __name__ == "__main__":
     main()


# 
# ---- Task Menu ----
# 1. Add New Task (i) title (ii) priority (iii) completed
# 2. List Tasks
# 3. Set Complete Task
# 4. Delete Task
# 5. Tasks Report
# 6. Save Tasks
# 7. exit (auto save (json))

# 11MM