# =>Exception Handling

# try:
#      # exception
# except exceptiontype:
#      #code handle the exception

# exceptiontype 
     # (i) ValueError
     # (ii) ZeroDivisionError 

# => General Exception
# try:
#      number = int(input("Enter lucky number:"))
#      print(f"Your lucky number is = {number}")
# except:
#      print("Something went wrong! Please enter a valid number.")


# => Specific Exception
# try:
#      number = int(input("Enter lucky number:"))
#      print(10/number)
# except ValueError:
#      print("Invalid input! Please enter a valid number.")
# except ZeroDivisionError:
#      print("You can't divide by zero")

# => else and finally

# else Block (Optional) = execute only if no exception occurs in the try block
# finally Block (Optional) = execute whether or not anyexception occurs

# try:
#      number = int(input("Enter lucky number:"))
#      # print(10/number)
#      result = 10/number
# except ValueError:
#      print("Invalid input! Please enter a valid number.")
# except ZeroDivisionError:
#      print("You can't divide by zero")
# else:
#      print(f"Result is = {result}")
# finally:
#      print("Program Completed")

# => Raising Exception
try:
     age = int(input("Enter your age: "))
     if age < 0:
          raise ValueError("Age can't be negative.")
     else:
          print(f"Your age is = {age}")
except ValueError as err:
     print(f"Error: {err}")