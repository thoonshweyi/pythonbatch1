# =>Unpacking Arguments

def sayhi(name,age):
     print(f"Hello friend! my name is {name}, i am {age} years old.")

# Unpacking positional argument
sayhi('Su Su',30)
args = ('Yu Yu',20)
sayhi(*args) #Hello friend! my name is Yu Yu, i am 20 years old.

def addingnumbers(a,b,c):
     print(f"Sum Result = {a+b+c}")
addingnumbers(1,2,3) #Sum Result = 6

tuplenmbers = (10,20,30) 
addingnumbers(*tuplenmbers) #Sum Result = 60

listnumbers = [100,200,300]
addingnumbers(*listnumbers) #Sum Result = 600

# Unpack keyword argument
listinfo = {"name":"Hla Hla","age":30}
sayhi(**listinfo) #Hello friend! my name is Hla Hla, i am 30 years old.
