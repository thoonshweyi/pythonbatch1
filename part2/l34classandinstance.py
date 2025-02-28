class Car:
     SPEED_LIMIT:float = 150

     def __init__(self,brand:str) -> None:
          self.brand = brand 
     
     def drive(self,*,speed:float) -> None: # Keyword-Only Arguments.  use by asterisk(*) key
          if speed > self.SPEED_LIMIT:
               print(f"Speed Limit activated: Driving at {self.SPEED_LIMIT} km/h")
          else:
               print(f"Driving at {speed}km/h")

def main() -> None:
     bmw: Car = Car("BMW")
     bmw.drive(speed=100)

     bmw.SPEED_LIMIT = 170
     bmw.drive(speed=160)
     bmw.drive(speed=200)

if __name__ == "__main__":
     main()

# 23CI