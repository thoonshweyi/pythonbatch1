# Function
# 1. Simple Function with No Parameters
# 2. Function with Parameter
          # (i) Single Parameter Function
          # (ii) Multi Parameter Function
# 3. Function with default Parameter
# 4. Function with a Return Value
# 5. Function with multi Return Values
# 6. Lambda Function (Anonymous Function)

def sayname():
     print("Hello Aung Aung")

sayname()
sayname()


# 2. Function with Parameter
#    (i) Single Parameter Function

def saycity(city):
     print("Hello "+city)

saycity("Yangon")
saycity("Mandalay")

# 3. Function with default Parameter
def country(country="Thailand"):
     print(f"Hello {country}")

country()
country("Myanmar")
country("Indonesia")

# 4. Function with a Return Value
def sayage():
     return "I am 25 years old"

print(sayage())


def saynickname():
     result = "Daw Pu"
     return result

print(saynickname())


def saynum(num1=20):
     return num1

print(saynum(100))
print(saynum())


def greeting(value="yamin"):
     return f"Hello {value}"

print(greeting("Su Su"))
print(greeting())
# Python offers a powerful feature called f-strings (formatted string literals) 
# They are called f-strings because you need to prefix a string with the letter 'f' to create an f- string.


def funone(num1,num2):
     result = num1+num2
     return result 

print(funone(10,20)) #30


def funtwo(num1,num2=200):
     result = num1+num2
     return f"Toal value is = {result}" 

print(funtwo(10)) #210
print(funtwo(10,20)) #30


# 5. Function with multi Return Values
def saynameandage():
     name = "Honey"
     age = 26
     city = "Yangon"
     return name,age,city

print(saynameandage()) #('Honey', 26)
# print(type(saynameandage()))  #<class 'tuple'>
name,age,city = saynameandage()
print(name) #Honey
print(age)  #26
print(city)  #26

# abcd,efgh = saynameandage()
# print(abcd) #Honey
# print(efgh)  #26

# In Python, functions can return multiple values by simply separating the return values with commas. When a function returns multiple values, they are packaged into a tuple. This tuple can then be unpacked into separate variables.
# Multiple values are returned as a tuple.
# You can unpack the tuple directly into separate variables.
# You can return different types of data (integers, strings, booleans, etc.) in a single return statement.
# *Returning values and Receiving value parameter must be the same


# 6. Lambda Function (Anonymous Function)
addresult = lambda num1,num2,num3: num1+num2+num3
print(addresult(200,300,400))

addresult = lambda num1,num2=200,num3=500: num1+num2+num3
print(addresult(200,300))
print(addresult(100))

# *No return keywork
# *No parenthesis in parameter
# *Not allowed multi lines


# inputval = input('Enter your name = ')
# msg = "Hello "+inputval
# msg = f"Hello {inputval}" #v2 (do not use)
# # msg = "Hello %s" %inputval
# print(msg)


# firstname = input("Enter First Name = ")
# lastname = input("Enter Last Name = ")
# fullname = "Hello %s%s"% (firstname,lastname) #v2
# fullname = "Hello %s %s"% (firstname,lastname) #v2
# fullname = f"Hello {firstname} {lastname}"
# print(fullname)

