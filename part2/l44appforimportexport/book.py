class Book:
     def __init__(self,title,author,year):
          self.title = title
          self.author = author 
          self.year = year

     def bookinfo(self):
          return f"{self.title} was written by {self.year}"

     # 12BT 