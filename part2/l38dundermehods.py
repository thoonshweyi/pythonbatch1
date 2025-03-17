# => Dunder Methods 

# => __len__(), __add__()
from typing import Self
class Article:
     def __init__(self,title:str,rating:int) -> None: # Dunder Method
          self.title = title 
          self.rating = rating 
     
     def __len__(self) -> int:
          return self.rating
     
     def __add__(self,other:Self) -> Self:
          combinedtitle:str = f"{self.title} & {other.title}"
          combinedrating:int = self.rating + other.rating

          return Article(combinedtitle,combinedrating)

def main()-> None: # function, outside of the class
     sport:Article = Article("This is sport article",3)
     news:Article = Article("This is new article",5)
     
     print(sport.title)
     print(len(sport))

     print(news.title)
     print(len(news))
     print(news.__len__()) #5 , not recommended

     mixarticles : Article = sport + news  # add dender method for + sign
     print(mixarticles.title) # This is sport article & This is new article
     print(mixarticles.rating) # 8


if __name__ == "__main__":
     main()

# => Object Comparison:
# __eq__ , equality
# __lt__ , less than 
# __gt__ , greater than

from typing import Self
class Mobile:
     def __init__(self,brand:str,price:int,color:str)-> None:
          self.brand = brand
          self.price = price
          self.color = color

     # def __eq__(self,other:Self) -> bool: #check one 1 parametere
     #      return self.price == other.price

     def __eq__(self,other:Self) -> bool: #check all parameters
          print("Current = ",self.__dict__)
          print("Other = ",other.__dict__)
          return self.__dict__ == other.__dict__
     
     def __lt__(self,other:Self)->bool:
          return self.price < other.price
     
     def __gt__(self,other:Self)->bool:
          return self.price > other.price

def main()-> None: # function, outside of the class
     mob1:Mobile = Mobile("Oppo",300,"blue")
     mob2:Mobile = Mobile("Oppo",400,"blue")
     
     print(mob1)
     print(mob2)
     print(mob1 == mob2)
     print(mob1 < mob2)
     print(mob1 > mob2)


if __name__ == "__main__":
     main()


# => __str__ , string
# => __repr__ , representation

class Person:
     def __init__(self,name:str,age:int)->None:
          self.name = name
          self.age = age 

     # def __repr__(self)->str:
     def __str__(self)->str:
          return f'Name is {self.name}. {self.age} year'
     
def main()->None:
     personObj:Person = Person("Hnin Hnin",25)
     print(personObj) # before repr, <__main__.Person object at 0x00000227CB76D1C0>
     print(repr(personObj)) # Name is Hnin Hnin. 25 year


if __name__ == "__main__":
     main()

# => indexing 
# __getitem__

class Worker:
     def __init__(self,names):
          self.names = names 

     def __getitem__(self,index):
          return self.names[index]
     
def main()->None:
     workerObj: Worker = Worker(["Aung Aung","Tun Tun","Kyaw Kyaw"])
     print(workerObj[0])
     print(workerObj[1])
     print(workerObj[2])

if __name__ == "__main__":
     main()

# => Deleting an Object
class People:
     def __init__(self,name):
          self.name = name 

     def __del__(self):
          print(f"{self.name} has been deleted.")
     
def main()->None:
     poepleObj: People = People("Linn Linn")
     del poepleObj

if __name__ == "__main__":
     main()


# Dunder methods (short for Double UNDERscore) in Python are special methods that have double underscores at the beginning and end of their names, like __init__, __str__, and __add__. They're also called magic methods or special methods.

# These methods are automatically called by Python in certain situations and allow you to customize the behavior of your objects.


#  def __eq__(self,other:Self)
# -



