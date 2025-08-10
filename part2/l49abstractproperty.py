from abc import ABC, abstractmethod

class Person(ABC):
     @property
     @abstractmethod
     def getrole(self):
          pass

# personObj = Person() # error

class Engineer(Person):
     @property
     def getrole(self):
          return "Professional Engineer"

engineerObj = Engineer()
print(engineerObj.getrole)

# => exercise 
class Vehicle(ABC):
     @property 
     @abstractmethod
     def wheels(self):
          pass 

     @abstractmethod
     def drive(self):
          pass

class Car(Vehicle):
     @property 
     def wheels(self):
          return 12 

     def drive(self):
          return "Bus is driving on 12 wheels"
     

carObj = Car()
print(carObj.wheels) # 12
print(carObj.drive()) # Bus is driving on 12 wheels

# => Abstract Readonly Property 
 
class Employee(ABC):
     @property
     @abstractmethod
     def id(self):
          pass 

class Developer(Employee):
     def __init__(self,empid):
          self._empid = empid # Protected attribute 

     @property
     def id(self):
          return self._empid
     
developerObj = Developer(1001)
print(developerObj.id) # 1001
# developerObj.id = 1002 # AttributeError: 'Developer' object has no attribute '_Developer__empid'
print(developerObj.id) # 1001


# => Abstract Read/Write Property 
class Product(ABC):
     @property
     @abstractmethod
     def price(self):
          pass

     @price.setter
     @abstractmethod
     def price(self,value):
          pass

class Book(Product):
     def __init__(self,price):
          self._price = price

     @property
     def price(self):
          return self._price
     
     @price.setter
     def price(self,value):
          if value < 0:
               raise ValueError("Price cannot be negative value")
          self._price = value

bookObj = Book(100)
print(bookObj.price)


bookObj = Book(50)
print(bookObj.price)

# bookObj.price = -10   # ValueError: Price cannot be negative value
