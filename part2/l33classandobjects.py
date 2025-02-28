class Car:                         # defining the class
     def __init__(self,brand:str,wheels:int) -> None: # the constructor __init__() type hint
          self.brand = brand
          self.wheels = wheels

     def engineon(self) -> None:
          print(f"Engine on : {self.brand}")

     def engineoff(self) -> None:
          print(f"Engine off : {self.brand}")
     
     def drive(self,km:float) -> None:
          print(f"Driving: {self.brand} for {km}km/h")
     
     def describe(self) -> None:
          print(f"{self.brand} is a car with {self.wheels} wheels")


def main() -> None:
     toyota: Car = Car("Toyota",4)
     toyota.engineon()
     toyota.drive(50)
     toyota.engineoff()

     honda: Car = Car("Honda",6)
     honda.engineon()
     honda.drive(30)
     honda.engineoff()
# main()

if __name__ == "__main__":
     main()

class Staff:
     def __init__(self,name:str,age:int,hascar:bool) -> None:
          print(f"My name is {name}, I am {age} years old.")
          self.name = name 
          self.age = age
          self.hascar = hascar
     
     def getinfo(self) -> None:
          print(f"Name is {self.name}, Age is {self.age}, car status {self.hascar}")

def main() ->None :
     staffObj1: Staff = Staff("Nu Nu",27,True)
     staffObj2: Staff = Staff("Tun Tun",30,True)

     staffObj1.getinfo()
     staffObj2.getinfo()

     print(staffObj1.name)
     print(staffObj1.age)
     print(staffObj1.hascar)

     print(staffObj2.name)
     print(staffObj2.age)
     print(staffObj2.hascar)

if __name__ == "__main__":
     main()