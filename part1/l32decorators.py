# => Decorators

# Function Decorator
def div1(x,y):
     return x/y
print(div1(10,2)) # 5.0
print(div1(2,10)) # 0.2

def div2(x,y):
     if y > x:
          return y/x
     else:
          return x/y
print(div2(10,2)) # 5.0
print(div2(2,10)) # 5.0


# decorator
def check(func):
     def inner(x,y):
          if y > x:
               return y/x
          return func(x,y)
     return inner

# method 1
def div3(x,y):
     return x/y

div4 = check(div3)

print(div4(10,2)) # 5.0
print(div4(2,10)) # 0.2

# method 2
@check
def div5(x,y):
     return x/y

print(div5(10,2))
print(div5(2,10))

# exercise
def mydecorator(func):
     def wrapper():
          print("Before the function run")
          func()
          print("After the function run")
     return wrapper

@mydecorator
def sayhi():
     print("Hello, Sir!")

sayhi()

# => Decorator with Arguments
# using while

def saymyname(count):
     def decorator(func):
          def wrapper(name):
               x = 0 #init
               while x < count:
                    func(name)
                    x += 1
          return wrapper
     return decorator

@saymyname(5)
def greet(name):
     print(f"Hello, {name}!")

greet("Yu Yu") # greet = saymyname(5)(greet)


def talkmyname(count):
     def decorator(func):
          def wrapper(name):
               for _ in range(count):
                    func(name)
          return wrapper
     return decorator

@talkmyname(3)
def greeting(name):
     print(f"Hello, {name}!")

greeting("Ni Ni") # greeting = talkmyname(5)(greeting)


def sumnumbers(count):
     def decorator(func):
          def wrapper(*args):
               for _ in range(count):
                    func(args)
          return wrapper
     return decorator

@sumnumbers(3)
def sumresults(numbers):
     total = sum(numbers)
     print(f"Sum result is = {total}")

sumresults(1,2,3,4,5,6,7,8,9,10)


# => Multiple Decorators

def setuppercase(func):
     def wrapper():
          return func().upper()
     return wrapper

def setexclamation(func):
     def wrapper():
          return func() + "!!!!aa"
     return wrapper

@setuppercase
@setexclamation
def sayhello():
     return "hello"

print(sayhello()) #hello 
#sayhello = setuppercase(setexclamation(sayhello))

# Multiple Decorators with Arguments
def setcounter(count):
     def decorator(func):
          def wrapper(name):
               for _ in range(count):
                    func(name)
          return wrapper
     return decorator

def prefix(val):
     def decorator(func):
          def wrapper(name):
               print(val,end=" ")
               return func(name)
          return wrapper
     return decorator

@setcounter(2)
@prefix("Dear:")
def saygreet(name):
     print(f"Hello, {name}")

saygreet('Kyipyar') # Dear: Hello, Kyi Pyar

# What is a Decorator Function in Python?
# A decorator function in Python is a special function that modifies or enhances the behavior of another function without changing its structure. It allows us to add extra functionality to a function in a reusable and clean way.

# How a Decorator Works
# A decorator is a function that takes another function as an argument.
# It wraps the original function inside another function (a wrapper).
# It can modify the behavior of the original function before or after calling it.
# The wrapper function is returned, replacing the original function.


# Understanding @check
# Using @check is functionally identical to manually assigning div5 = check(div5). It applies the check decorator to div5 at the time of function definition.

# Decorators are applied from bottom to top (inside-out like nested function calls).


# def mydecorator(func):
#      def wrapper(name):
#           for _ in range(4):
#                func(name)
#      return wrapper

# @mydecorator
# def sayhola(name):
#      print(f"Hello, {name}")

# sayhola('Thorn')