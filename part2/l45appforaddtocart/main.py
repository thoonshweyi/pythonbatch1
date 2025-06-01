from models.book import Book
from models.user import User
from models.uitilities import gettitles,specialdiscount
# from models.uitilities import *



def main():
     bookObj1 = Book("Python","Daw Win Win",20,500)
     bookObj2 = Book("Djago","U Tun Tun",40,800)
     bookObj3 = Book("Open AI","Daw Hnin Hnin",50,1000)

     specialdiscount(bookObj1)
     specialdiscount(bookObj2)

     user = User("Ya Min")
     user.addtocart(bookObj1)
     user.addtocart(bookObj2)

     print("Book Titles: ",gettitles(user.carts))
     print(f"Total pages in book 1 = {len(bookObj1)}")
     print(f"Total pages in book 2 = {len(bookObj2)}")

     print(user)

     print(f"Total price {user.totalprice():.2f}")
if __name__ == "__main__":
     main()





# Book
# User

# Original Price: 100
# After Dis Price: 
# Book Title: [,,,]
# book 1 pages: 10
# book 2 pages: 15
# book 3 pages: 15
# User: Su Su, Card: ["Story One by nu"]


# *result
# Original Price = 20.00
# After Discount Price = 18.00
# Original Price = 40.00
# After Discount Price = 36.00
# Book Titles:  ['Python', 'Djago']
# Total pages in book 1 = 500
# Total pages in book 2 = 800
# User: Ya Min, Card: ['Python by Daw Win Win', 'Djago by U Tun Tun']
# Total price 54.00