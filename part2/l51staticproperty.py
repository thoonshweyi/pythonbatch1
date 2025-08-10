# Static Property (Class variable)

# exe 1
class BankAccount:
     # Static Property
     totalaccounts = 0
     def __init__(self,owner,balance=0):
          self.owner = owner
          self.balance = balance
          BankAccount.totalaccounts += 1

accObj1 = BankAccount("Su Myat",100)
accObj2 = BankAccount("Min Min",100)

print("Total bank accounts = ",BankAccount.totalaccounts) #Total bank accounts =  2

# exe 2
class Car:
     totalcars = 0 # static property / class property / class variable

     def __init__(self,brand):
          self.brand = brand
          Car.totalcars += 1

carObj1 = Car("Toyota")
carObj2 = Car("Honda")
carObj3 = Car("Suzuki")

print("Total cars models = ",Car.totalcars)

# exe3
class Counter():
     count = 0
     def __init__(self):
          Counter.count += 1

     @staticmethod
     def getcount():
          return Counter.count

counterObj1 = Counter()
counterObj2 = Counter()
counterObj3 = Counter()
counterObj4 = Counter()

print("Total object instance = ",Counter.getcount())

# => Custom Static Property 
class customstcproperty:
     def __init__(self,func):
          self.func = func

     # def __get__(self.obj,cls=None):
     #      return self.func()

class Greet:
     @customstcproperty
     def sayhi():
          return "Hello Mandalay!"
     
print(Greet.sayhi)


# Custom Static Property (with param)
class stcproperty:
     def __init__(self,func):
          self.func = func

     def __get__(self,obj,cls=None):
          return self.func(cls)

class NumCounter:
     idx = 100
     
     @stcproperty
     def getidx(cls):
          return cls.idx
     
print(NumCounter.getidx)