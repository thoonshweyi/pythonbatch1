class Task:
     def __init__(self,title,priority=1):
          self.title = title
          self.priority = priority
          self.completed = False

class TaskJob:
     def __init__(self):
          self.tasks = []

     def addnewtask(self,title,priority=1):
          self.tasks.append(Task(title,priority))

     def listtasks(self):
          if not self.tasks:
               print("No tasks found.")
               return
          for idx,task in enumerate(self.tasks):
               status = "Finished" if task.completed else "Pending"
               print(f"{idx+1}. {task.title}, (Prioriy: {task.priority}) {status}")
          
     def setcompletask(self,index):
          try:
               
          except IndexError:
               print("Invalid task number!")

     def deletetask(self,index):
          try:
          
          except IndexError:
               print("Invalid task number!")

     def taskreport(self):
          try:
          
          except IndexError:
               print("Invalid task number!")

     def savetasks(self,filename):
          try:
          
          except IndexError:
               print("Invalid task number!")