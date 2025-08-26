class Car:                                             # defining the class
     def __init__(self,brand:str,wheels:int)->None: #the constructor __init__() type hint
          self.brand = brand
          self.wheels = wheels

     def engineon(self) -> None:
          print(f"Engine on: {self.brand}")

     def engineoff(self) -> None:
          print(f"Engine off: {self.brand}")

     def drive(self,km:float)->None:
          print(f"Driving: {self.brand} for {km}km/h.")

     def describe(self)->None:
          print(f"{self.brand} is a car with {self.wheels} wheels.")

def main()->None:
     toyota:Car = Car("Toyota",4)
     toyota.engineon() 
     toyota.drive(50) 
     toyota.engineoff() 

     honda:Car = Car("Honda",6)
     honda.engineon() 
     honda.drive(30) 
     honda.engineoff() 

if __name__ == "__main__":
     main()


class Staff:
     def __init__(self,name:str,age:int,hascar:bool)->None:
          print(f"My name is {name}, I am {age} years old.")
          self.name = name
          self.age = age
          self.hascar = hascar

     def getinfo(self)->None:
          print(f"Name is {self.name}, Age is {self.age}, car status {self.hascar}")

def main()->None:
     staffObj1 = Staff("Nu Nu",27,True)
     staffObj2 = Staff("Tun Tun",30,False)

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


# 1. What is __name__ in Python?

#      Every Python file (a module) automatically gets a special variable called __name__.

#      Its value depends on how the file is used.

#      👉 If you run the file directly:

#      python myfile.py


#      then Python sets:

#      __name__ == "__main__"


#      👉 If you import the file into another file:

#      import myfile


#      then Python sets:

#      __name__ == "myfile"

# 2. Why check if __name__ == "__main__": ?

#      It’s a way to say:

#      “Run this part only if this file is the main program, not when it’s imported.”

#      This avoids running code by accident when the file is imported.

# 3. Example

#      car.py

#      class Car:
#      def __init__(self, brand):
#           self.brand = brand

#      def describe(self):
#           print(f"This car is {self.brand}")

#      def main():
#      toyota = Car("Toyota")
#      toyota.describe()

#      # 👇 this block runs only if car.py is executed directly
#      if __name__ == "__main__":
#      main()


#      test.py

#      import car   # only imports the class, doesn’t run main()

#      print("In test.py now")
#      mycar = car.Car("Honda")
#      mycar.describe()

# 4. What happens?

#      Run directly:

#      python car.py


#      Output:

#      This car is Toyota


#      Run through import:

#      python test.py


#      Output:

#      In test.py now
#      This car is Honda


#      Notice: main() from car.py did not run, because when car.py is imported, its __name__ is "car", not "__main__".