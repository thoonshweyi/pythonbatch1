
from functools import reduce
class User:
     def __init__(self,name):
          self.name = name 
          self.carts = []

     def addtocart(self,book):
          self.carts.append(book)

     def totalprice(self):
          return reduce(lambda x,book: x+book.getprice(),self.carts,0)
     
     def __str__(self):
          return f"User: {self.name}, Card: {[ str(book) for book in self.carts ]}" 