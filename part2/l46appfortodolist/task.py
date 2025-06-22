import json 
from functools import reduce

class Task:
     def __init__(self,title,priority=1):
          self.title = title
          self.priority = priority
          self.completed = False

     def setdict(self):
          return {"title":self.title,"priority":self.priority,"completed":self.completed}

     def getdict(data):
          task = Task(data['title'],data['priority'])
          task.completed = data['completed']
          return task

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
               self.tasks[index -1 ].completed = True
          except IndexError:
               print("Invalid task number!")

     def deletetask(self,index):
          try:
               del self.tasks[index - 1]
          except IndexError:
               print("Invalid task number!")

     def taskreport(self):
          completed = list(filter(lambda task: task.completed, self.tasks))
          total = len(self.tasks)
          percent =   (len(completed) / total * 100) if total else 0
          print(f"Total tasks: {total}, Completed: {len(completed)}, Percent: {percent:.2f} %")
          
          highpriorities = reduce(lambda x,y: x+(1 if y.priority >= 5 else 0),self.tasks,0)
          print(f"Total high priority tasks (over 4): {highpriorities}")

     def savetasks(self,filename):
          try:
               with open(filename,'w') as file:
                    json.dump([task.setdict() for task in self.tasks], file)
               print("Task saved.")
          except TypeError as e:
               print("Error: Type Error: ",str(e))
          except Exception as e:
               print("Error Saving File: ",str(e))
     def loadfile(self,filename):
          try:
               with open(filename,'r') as file:
                    datas = json.load(file)
                    self.tasks = list(map(Task.getdict(),datas))
               print("Tasks file loaded.")
          except FileNotFoundError:
               print("No saved tasks file found.")
          except Exception as e:
               print("Error loading file: ",e)
     
