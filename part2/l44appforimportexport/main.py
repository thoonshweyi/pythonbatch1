from manage import BookManage

def main():
     manage = BookManage()

     # Add book
     manage.addbook("Book One","Aung Aung",2020)
     manage.addbook("Book Two","Aung Aung",2020)
     manage.addbook("Book Three","Su Su",2021)
     manage.addbook("Book Four","Yu Yu",2022)
     manage.addbook("Book Five","Yu Yu",2022)
     manage.addbook("Book Six","Yu Yu",2023)


     # List books 
     manage.listbooks()

     # Search by author
     authorname = 'yu yu'
     filterresults = manage.searchbyauthor(authorname)
     print(f"Books by {authorname}: ")

     for book in filterresults:
          print(f"{book.title} publish in {book.year}")


if __name__ == "__main__":
     main()