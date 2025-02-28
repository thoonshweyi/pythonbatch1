# =>Type of Argument in Python
# Positional Arguments
# Keyword Arguments
# Default Arguments
# Variable-length Arguments (*args) (Non-keywork Variable Arguments)
# Variable-length Arguments (**kwargs) (keywork Variable Arguments)

# Positional Arguments
def greet(name,age):
     print(f"Hello friends! my name is {name}, i am {age} years old.")

greet("Su Su",23) #Hello friends! my name is Su Su, i am 23 years old.
greet(25,"Nu Nu") #Hello friends! my name is 25, i am Nu Nu years old.

# Keyword Arguments
def hifi(name,age):
     print(f"Hello friends! my name is {name}, i am {age} years old.")

hifi(name="Min Min",age=25) #Hello friends! my name is Min Min, i am 25 years old.
# hifi(name="Min Min",ages=25)
hifi(age=25,name="Nyi Nyi") #Hello friends! my name is Nyi Nyi, i am 25 years old.


# Default Arguments
def hime(name,age=18):
     print(f"Hello friends! my name is {name}, i am {age} years old.")

hime(name="Yamin") #Hello friends! my name is Yamin, i am 18 years old.
hime(name="Thuzar",age=20) #Hello friends! my name is Thuzar, i am 20 years old.

# Variable-length Arguments (*args) (Non-keywork Variable Arguments)
def boys(*args):
     print(args)

boys("aung aung") #('aung aung',)
boys("aung aung","kyaw kyaw") #('aung aung', 'kyaw kyaw')
boys("aung aung","kyaw kyaw","zaw zaw","tun tun") #('aung aung', 'kyaw kyaw', 'zaw zaw', 'tun tun')
# boys("aung aung",args="kyaw kyaw") #error when including Keywork Arguments

def sumresults(*numbers):
     total = sum(numbers)
     print(f"Sum result is = {total}")

sumresults(1,2,3) # Sum result is = 6
sumresults(10,20,30,40,50) #Sum result is = 150

# Error
# def myfunone(*nums,num):
def myfunone(num,*nums):
     print(num)  #1
     print(nums) #(2, 3, 4, 5)
myfunone(1,2,3,4,5)



# Variable-length Arguments (**kwargs) (keywork Variable Arguments)
def personinfos(**kwargs):
     for key,value in kwargs.items():
          print(f"{key} = {value}")
personinfos(name="Thuzar",age=25,city="Mandalay")
personinfos(name="Kaung Kaung",professional="Engineer",city="Yangon")

# Exercise (Combine Different Type if Auguments)
def emailsender(address,*messages,**files):
     print(f"Address = {address}")
     if messages:
          for message in messages:
               print(f"Message = {message}")
     if messages:
          for key,value in files.items():
               print(f"{key} = {value}")

# emailsender("dataland@gmail.com")
emailsender("dataland@gmail.com","Hellow admin","i want to request vdo records",lesson="Python B1",classdate="25/Nov/2024")

def studentinfos(name,age=18,*hobbies,**infos):
     print(f"Name = {name}")
     print(f"Age = {age}")
     if hobbies:
          for hobbie in hobbies:
               print(f"Hobbie = {hobbie}")
     if infos:
          for key,value in infos.items():
               print(f"{key} = {value}")

studentinfos("Nandar")
studentinfos("Maung Maung",25)
studentinfos("Aung Kyaw",25,"reading","travelling")
studentinfos("Kyaw Kyaw",25,"reading","travelling",city="Bago",profession="Engineer")



def staffinfos(name,age=18,*hobbies,**infos):
     print(f"Name = {name}")
     print(f"Age = {age}")
     if hobbies:
               # print(f"Hobbie = {hobbies}") #Hobbie = ('reading', 'travelling')
               print(f"Hobbie = {','.join(hobbies)}")
     if infos:
          for key,value in infos.items():
               print(f"{key} = {value}")

staffinfos("Ni Lar",20,"reading","travelling",city="Yangon",profession="Engineer")
# 25OV