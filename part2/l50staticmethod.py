class CalUtilites:
     @staticmethod
     def addresult(x,y):
          return x + y
     
     @staticmethod
     def iseven(num):
          return num% 2 == 0
     

print(CalUtilites.addresult(10,5))# 15
print(CalUtilites.iseven(10)) # True
print(CalUtilites.iseven(9)) # False

# exercise
class EmailValidator:
     @staticmethod
     def isemail(email):
          return "@" in email and "." in email

     @staticmethod
     def ispositiveint(num):
          return isinstance(num,int) and num > 0

print(EmailValidator.isemail("dataland@gmail.com"))
print(EmailValidator.ispositiveint(1))
print(EmailValidator.ispositiveint(-1))




# Method Type            Decorator           First Parameter
# Instance Method        None                self
# Abstract Method        @abstractmethod     self
# Static Method          @staticmethod       None
# Class Method           @classmethod        cls


# 6SM