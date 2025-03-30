from random import choice
from time import sleep
class GreenlightRedlight:
     def __init__(self):
          self.moves = 0
          self.maxmoves = 5

     def startgame(self):
          print('Welcome to Green Light Red Light Game')
          print("Type 'move' when it's Green Light, but stay still (type Enter key) if you see Red Light!") 
          print("Type 'exit' to quit.")

          sleep(2) # time for each light
          while self.moves < self.maxmoves:
               getlight = choice(["Green Light","Red Light"])
               print(f"{getlight}")

               if getlight == "Green Light":
                    # sleep(2) # Timer 2=2 second
                    playeraction = input('You action: ').lower()
                    if playeraction == 'move':
                         self.moves += 1
                         print(f"Good job! Moves: {self.moves}/{self.maxmoves}")
                    elif playeraction == 'exist':
                         print('Thanks for playing!')
                         break
                    else:
                         print("Game over!!!, you missed the Green Light.")
                         break
               elif getlight == "Red Light":
                    # sleep(2) # Timer 2=2 second

                    print("Red Light ! Don't move")
                    playeraction = input('You action: ').lower()

                    if playeraction == 'move':
                         print("Grme over!!!, You moved on REd Light.")
                    elif playeraction == 'exist':
                         print('Thanks for playing!')
                         break 
          
          if self.moves >= self.maxmoves:
               print('Congratulation! You won')

def main():
     game:GreenlightRedlight = GreenlightRedlight()
     game.startgame()

if __name__ == "__main__":
     main()


# google drive