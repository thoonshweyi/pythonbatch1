from datetime import datetime
from random import choice
class Chat: 
     def __init__(self,name:str,version:float)->None:
          self.name = name 
          self.version = version 

     def botinfo(self)->str:
          return f"{self.name} is a bot. Version is {self.version} beta."
     
     def conversations(self,text:str) -> str:
          gettext:str = text.lower()

          if 'hello' in gettext:
               return f'{self.name}: Hey there!'
          elif 'how old are you' in gettext:
               return f'{self.name}: I am version {self.version}'
          elif 'what time is it' in gettext:
               getnow: datetime = datetime.now()
               # return f'{self.name}: The current time is {getnow.strftime('%H:s%M:%S')}'
               return f'{self.name}: The current time is {getnow:%H:%M:%S}'
     
          elif 'bye' in gettext:
               return f"{self.name}: See you later!"
          else:
               randomresponse:list[str] = ["I don't understand!","What?","I don't know","Repeat again!"]
               return f'{self.name}; {choice(randomresponse)}'
          

     def startrun(self)->None:
          while True:
               getinputext:str = input('You: ')

               if getinputext.lower() == 'exit':
                    print('Thank you for chatting with us. See you later.')
                    break
               else:
                    response: str = self.conversations(getinputext)
                    print(response)

def main()-> None:
       chatObj: Chat = Chat("Javic",1.0)
       print(chatObj.botinfo())
       chatObj.startrun()

if __name__ == "__main__":
       main()


# 16AC