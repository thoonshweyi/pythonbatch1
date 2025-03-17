class Car:                         # defining the class
     def __init__(self,brand:str,wheels:int) -> None: # the constructor __init__() type hint
          self.brand = brand  # public attrubute
          self._wheels = wheels # protected attribute
          self.__enginestatus = False # private attrubute

     def engineon(self) -> None:
          self.__enginestatus = True
          print(f"Engine on : {self.brand}")


     def engineoff(self) -> None:
          self.__enginestatus = False
          print(f"Engine off : {self.brand}")
     
     def drive(self,km:float) -> None:
          if self.__enginestatus == True:
               print(f"Driving: {self.brand} for {km}km/h")
          else: 
               print(f"Cannot Drive: {self.brand} engine is off")

     def describe(self) -> None:
          print(f"{self.brand} is a car with {self._wheels} wheels")

     def __checkcomputerbox(self)->None: #Instance Private Methods
          print(f'Checking Computer Box of {self.brand}!')

     def _serviceengine(self)->None: #Instance Protected Methods
               print(f'Servicing the engine of {self.brand}!')

     def maintenance(self)->None: # Instance public Methods (as getter)
          print(f"Maintenance on {self.brand}!")
          self.__checkcomputerbox()
          self._serviceengine()

def main() -> None:
     toyota: Car = Car("Toyota",4)
     toyota.engineon()
     toyota.drive(50)
     toyota.engineoff()
     toyota.describe()

     # print(f"This is protected attribute = {toyota._wheels}")
     # print(f"This is protected attribute = {toyota.__enginestatus}") #error
     # print(f"This is protected attribute = {toyota._Car__enginestatus}") #not recommended, This is private attribute

     # toyota._serviceengine()
     # toyota.__checkcomputerbox() # error
     # toyota._Car__checkcomputerbox() # error

     toyota.maintenance()

# main()

if __name__ == "__main__":
     main()


# js
# Modifier     Syntax         Access Inside Class      Access Inside Subclass   Access Outside Class
# Public       this.name      Yes                      Yes                      Yes
# Private      #name          Yes                      No                       No
# Protected    _name          Yes                      Yes                      Possible (should not use)



# Modifier     Syntax         Access Inside Class      Access Inside Subclass   Access Outside Class
# Public       self.name      Yes                      Yes                      Yes
# Private      self.__name    Yes                      No                       No
# Protected    self._name     Yes                      Yes                      Possible (should not use)

# 2AM