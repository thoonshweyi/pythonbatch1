class Book:
     def __init__(self,title,author,price,pages):
          self.title = title
          self.author = author
          self._price = price # protected
          self.__pages = pages # private

     def getprice(self):
          return self._price 
     
     def getpages(self):
          return self.__pages
     
     def applydiscount(self,discount):
          #self._price -= self._price * discount / 100
          self._price -= self._price * discount

     def __str__(self):
          return f"{self.title} by {self.author}"

     def __len__(self):
          return self.__pages

# 100 * 10 / 100 = 10, 100 - 10 = 90
# 100 & 0.1 = 10, 100 - 10 = 90