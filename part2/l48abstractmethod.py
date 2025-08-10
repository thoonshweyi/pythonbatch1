# Must be impleented by concrete subclasses
# Can't be instantiated directly

# Create an "Abstract Base Class" (ABC)

from functools import reduce
from abc import ABC, abstractmethod
class Person(ABC):
     def __init__(self,name,age) -> None:
          self.name = name
          self.age = age

     @abstractmethod #decorator
     def showinfo(self)->None:
          # pass    # (no implementation here)
          ...       # (ellipsis = more to come or used in special case)
          
     @abstractmethod
     def getrole(self)->None:
          #pass 
          ...

class Student(Person):
     def __init__(self,name,age,studentid,major)->None:
          super().__init__(name,age)
          self.studentid = studentid
          self.major = major

     #implement the abstract methods
     def showinfo(self):
          return f"Student: {self.name}, Age: {self.age}, ID: {self.studentid}, Major: {self.major}"

     def getrole(self):
          return "Student"
     
class Employee(Person):
     def __init__(self,name,age,employeeid,department):
          super().__init__(name,age)
          self.employeeid = employeeid
          self.department = department

     def showinfo(self):
          return f"Employee: {self.name}, Age: {self.age}, ID: {self.employeeid}, Department: {self.department}"

     def getrole(self):
          return "Employee"
     

class Teacher(Employee):
     def __init__(self,name,age,employeeid,department,subject):
          super().__init__(name,age,employeeid,department)
          self.subject = subject

     def showinfo(self):
          return f"Teacher: {self.name}, Age: {self.age}, ID: {self.employeeid}, Department: {self.department}, Subject: {self.subject}"

     # def getrole(self):
     #      return "Teacher" # Teacher (id disabled ! result = Eployee)


class Staff(Employee):
     def __init__(self,name,age,employeeid,department):
          super().__init__(name,age,employeeid,department)


     def showinfo(self):
          return f"Staff: {self.name}, Age: {self.age}, ID: {self.employeeid}, Department: {self.department}"

     # def getrole(self):
     #      return "Staff"

def main()->None:
     student: Student = Student("Hnin Hnin",18,"ST1001","Computer Science")
     employee: Employee = Employee("Linn Linn",25,"EM2002","HR")
     teacher: Teacher = Teacher("Win Win",55,"TR3003","Mathematic","Math")

     
     print(student.showinfo()) # Student: Hnin Hnin, Age: 18, ID: ST1001, Major: Computer Science
     print(student.getrole()) # Student

     print(employee.showinfo()) # Employee: Linn Linn, Age: 25, ID: EM2002, Department: HR
     print(employee.getrole()) # Employee

     print(teacher.showinfo()) # Teacher: Win Win, Age: 55, ID: TR3003, Department: Mathematic, Subject: Math
     print(teacher.getrole()) # Teacher

if __name__ == "__main__":
     main()

# => addition exercise
class RoleManager:
     def __init__(self):
          self.peoples = []

     def addperson(self,person):
          if not isinstance(person,Person):
               raise TypeError("Only Person subclass can be added")
          self.peoples.append(person)

     def displayall(self):
          for people in self.peoples:
               print(people.showinfo())

     def countbyrole(self,role):
          # return sum(1 for people in self.peoples if people.getrole() == role)
          return reduce(lambda x,y: x+ (1 if y.getrole() == role else 0),self.peoples,0)

rolemanagerObj =  RoleManager()
rolemanagerObj.addperson(Student("Nilar",20,"ST1002","Physics"))
rolemanagerObj.addperson(Employee("Malar",30,"EM2003","Marketing"))
rolemanagerObj.addperson(Teacher("Kyipyar",50,"TR3004","Science","Biology"))
rolemanagerObj.addperson(Staff("Muyar",55,"EM2004","Marketing"))

rolemanagerObj.displayall()

print(f"Number of students: {rolemanagerObj.countbyrole("Student")}")
print(f"Number of employees: {rolemanagerObj.countbyrole("Employee")}")

