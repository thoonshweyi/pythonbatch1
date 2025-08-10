


class Greeting:
     @classmethod
     def sayhello(cls):
          print(f"Hello from {cls.__name__}")


Greeting.sayhello()

# exe 2
class Mobile:
     network = "5G"

     @classmethod
     def getconnection(cls):
          return cls.network
     
print(Mobile.getconnection())

mobileObj:Mobile = Mobile()
print(mobileObj.getconnection())

# exe3 (static property + classmethod)
class Counter:
     count = 0

     def __init__(self):
          Counter.count += 1

     @classmethod
     def getcount(cls): # cls refers to the class itself
          return cls.count

print(Counter.getcount()) # 0 # before instantiation

counterObj1 = Counter()
counterObj2 = Counter()
counterObj3 = Counter()

print(Counter.getcount()) # 3 # after instant also valid, but less common (for static methods, class methods you don' need to create an object)

# exe 4
class Book:
     BOOKTYPES = ("HardCover","PaperBack","Ebook")

     @classmethod
     def booktypevalid(cls,formatname):
          return formatname in cls.BOOKTYPES
     

print(Book.booktypevalid("PDF")) # False
print(Book.booktypevalid("Paperback")) # False
print(Book.booktypevalid("Ebook")) # True

# => Alternative Constructor

class Person:
     def __init__(self,name,age):
          self.name = name
          self.age = age

     @classmethod
     def calculateage(cls,name,birthyear):
          currentyear = 2025
          age = currentyear - birthyear
          return cls(name,age)

     @classmethod
     def currentage(cls,name,birthyear):
          from datetime import date
          currentyear = date.today().year
          age = currentyear - birthyear
          return cls(name,age)
     
# Normal instant
# personObj1 = Person("Nu Nu",25) # Nu Nu 25
# print(personObj1.name, personObj1.age)

# Using class method as alternative constructor
personObj2 = Person.calculateage("Yu Yu",1995)
print(personObj2.name,personObj2.age) # Yu Yu 30

personObj3 = Person.currentage("Hla Hla",1996)
print(personObj3.name,personObj3.age) 

# => Class Method with Inheritance
class Student:
     def __init__(self,name):
          self.name = name

     @classmethod
     def describe(cls,level):
          return f"A {cls.__name__} studies at {level} level."
     
class GraduateStudent(Student):
     pass

print(Student.describe("undergraduate")) # A Student studies at undergraduate level.
print(GraduateStudent.describe("graduate")) # A GraduateStudent studies at graduate level.


# exe 2
class Vehicle:
     vehicletype = "Unknown"

     @classmethod
     def describe(cls):
          return f"This is a {cls.vehicletype} vehicle."
     
class Car(Vehicle):
     vehicletype = "Car"

print(Car.describe()); # This is a Car vehicle.

# exe 3
class ProLanguage:
     langtype = "Generic Language"

     @classmethod
     def getlang(cls):
          return f"This is {cls.langtype}"

class JavaScript(ProLanguage):
     langtype = "JavaScript"


class Python(ProLanguage):
     langtype = "Python"

print(ProLanguage.getlang()) #This is Generic Language
print(JavaScript.getlang()) # This is JavaScript
print(Python.getlang()) # This is Python


# =>  Define Read-Only Property (@property)

# exe 1
class Employee:
     def __init__(self,name,monthlysalary):
          self.name = name 
          self._monthlysalary = monthlysalary

     @property
     def annualsalary(self):
          return self._monthlysalary * 12
     
employeeObj = Employee("Zaw Zaw",500)
print(employeeObj.annualsalary) #6000

# employeeObj.annualsalary = 10000
# print(employeeObj.annualsalary)

# exe 2 (@property with Getter and Setter)

class Staff:
     def __init__(self,name):
          self._name = name

     @property
     def name(self):
          return self._name.upper()
     
     @name.setter
     def name(self,newname):
          self._name = newname

staffObj = Staff('Yu Yu')
print(staffObj.name) # YU YU

staffObj.name = "Nu Nu"
print(staffObj.name) # NU NU

