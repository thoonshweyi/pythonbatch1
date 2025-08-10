class classproperty:
     def __init__(self,func): # stores the function
          self.func = func

     def __get__(self,obj,cls=None): # make it work like a property (no () needed)
          return self.func(cls)
     
class Greet:
     _greeting = "Hello Mandalay!"

     @classproperty
     def sayhi(cls):
          return cls._greeting
     
print(Greet.sayhi)

# Method override in Subclass
class SocialMedia:
     @classproperty
     def category(cls):
          return "Generic Social Platform"
     

class Facebook(SocialMedia):
     @classproperty
     def category(cls):
          return "Social Network"
     
class YouTube(SocialMedia):
     @classproperty
     def category(cls):
          return "Video Sharing"
     

print(SocialMedia.category) #Generic Social Platform
print(Facebook.category) # Social Network
print(YouTube.category) #Video Sharing

# 3CP
