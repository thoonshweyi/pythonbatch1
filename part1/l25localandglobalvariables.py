# => Global Variable

globalval = "I am global"

def myfun1():
     print("Inside function myfun1 =",globalval)
myfun1()
print("Outside function myfun1 =",globalval)

# => Local Variable 

def myfun2():
     localval = "I am local"
     print("Inside function myfun2 = ",localval)
myfun2() #I am local
# print(localval) # NameError: name 'localval' is not defined. 

# => Same Name for Local and Global Variable 
globalvar = "I am Global"
def myfun3():
     globalvar = "I am Local"
     print("Inside function myfun3 = ",globalvar)

myfun3() # I am Local
print("Outside function myfun3 = ",globalvar) # I am Global

# => Exercise (including gloval Keyword)
msg1 = "Hello Sir, this is global variable"
def funone():
     msg2 = "His Students, this is local variable"

     print("Inside function funone = ",msg1)
     print("Inside function funone = ",msg2)

def funtwo():
     msg1 = "Hello Teacher, Teacher is global variable"
     msg2 = "Hello Staffs, this is local variable"

     print("Inside function funtwo = ",msg1)
     print("Inside function funtwo = ",msg2)

def funthree():
     global msg1
     msg1 = "Hello Boss, Teacher is global variable"
     msg2 = "Hello Employee, this is local variable"

     print("Inside function funtwo = ",msg1)
     print("Inside function funtwo = ",msg2)


funone()
funtwo()
# print("Outside function funtwo = ",msg2) # NameError: name 'msg2' is not defined.

print("Outside function before funthree = ",msg1) 
funthree()
print("Outside function after funthree = ",msg1) 

# => Nested Function and nonlocal Keyword
def funfour():
     msg3 = "i am msg3 from outside funfive"

     def funfive():
          nonlocal msg3
          msg3 = "i am msg3 Modified by funfive"
     
     print("Before invoking funfive = ",msg3)
     funfive()
     print("Before invoking funfive = ",msg3)

funfour()


# nonlocal Keyword in Python
# The nonlocal keyword is used in nested functions to indicate that a variable is not local to the inner function but belongs to an enclosing (non-global) scope. It allows modifying variables defined in the outer (but not global) function.

# Why Use nonlocal?
# By default, Python treats variables inside a function as local. If you try to modify a variable from an outer function without nonlocal, it creates a new local variable instead of modifying the outer one.

# Using nonlocal allows us to update variables from the enclosing function without making them global.