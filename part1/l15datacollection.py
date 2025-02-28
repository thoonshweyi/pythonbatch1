# =>Data Collections (Module Containers)

from collections import Counter
getcounts = Counter("Hello World")
print(getcounts) # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})

# => Queues (from collections module)

from collections import deque

qpersons = deque(["Su Su","Nu Nu","Yu Yu"])
print(qpersons)
qpersons.append("Tun Tun") # Add to right end
qpersons.appendleft("Sai Sai") # Add to left start

# for person in qpersons:
#      print(person)

# Removing elements 
qpersons.pop() # Remove from right end
qpersons.popleft() # Remove from left end
for person in qpersons:
     print(person)

# defaultiict (from collections module)
from collections import defaultdict

items = defaultdict(list)

items['fruits'].append('apple')
items['fruits'].append('mango')
items['fruits'].append('banana')
items['colors'].append('orange')


print(items["fruits"]) # ['apple', 'mango', 'banana']
print(items["colors"]) # ['orange']
print(items["candy"]) # []



# 11POV

# Grouingp Items
groups = defaultdict(list)
foods = [("fruit","apple"),("fruit","orange"),("vegatable","carrot"),("fruit","mango")]


for key,value in foods:
     groups[key].append(value)

print(groups) # defaultdict(<class 'list'>, {'fruit': ['apple', 'orange', 'mango'], 'vegatable': ['carrot']})



# numitems = defaultdict(int)
# numitems['val'] += 1
# print(numitems)
# print(numitems["val"]) # 1


numitems = defaultdict(int)
print(numitems["val"]) # 0
numitems['val'] = 1
print(numitems["val"]) # 1

# Counting Elements 
colorcounts = defaultdict(int)
candycolors = ["red","green","blue","green","red","black","green"]

for candycolor in candycolors:
     colorcounts[candycolor] += 1
print(colorcounts) #defaultdict(<class 'int'>, {'red': 2, 'green': 3, 'blue': 1, 'black': 1})

# =>OrderedDict (from collections module)
from collections import OrderedDict
myorders = OrderedDict()
myorders["num1"] = 100
myorders["num2"] = 200
myorders["num3"] = 300
myorders["num4"] = 400
myorders["num5"] = 500

print(myorders) #OrderedDict({'num1': 100, 'num2': 200, 'num3': 300, 'num4': 400, 'num5': 500})
print(myorders["num2"]) #200

#Reordering Item
myorders.move_to_end("num2")
print(myorders) #OrderedDict({'num1': 100, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200})

# re-inserting 
myorders["num1"] = 110
print(myorders) #OrderedDict({'num1': 110, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200})

#Removing Item
del myorders["num3"]
print(myorders) #OrderedDict({'num1': 110, 'num4': 400, 'num5': 500, 'num2': 200})

config = OrderedDict()
config['host'] = "localhost"
config['port'] = 8080
config['debug'] = True

for key,value in config.items():
     print(f"{key} : {value}")

# => nameTuple (from collections module)
from collections import namedtuple

LuckyNumbers = namedtuple("LuckyNumbers",["num1","num2","num3"])

getnums = LuckyNumbers(33,66,99)
print(getnums.num1) # 33
print(getnums.num2) # 66
print(getnums.num3) # 99

# exercise with tuple , hard to remember what index number represents
staff = ("Yu Yu",20,"Developer")
print(staff[0]) # Yu Yu
print(staff[1]) # 20
print(staff[2]) # Developer

#namedtuple
Student = namedtuple("Student",["name","age","profession"])
# pupil = Student("Su Su",30,"Engineer")
pupil = Student(name="Su Su",age=30,profession="Engineer")

print(pupil.name) # Su Su
print(pupil.profession) # Engineer
print(pupil.age) # 30

# => ChainMap (from collection module)
from collections import ChainMap 

dict1 = {"name":"Aye Aye"}
dict2 = {"city":"Yangon"}
getdata = ChainMap(dict1,dict2)
print(getdata) #ChainMap({'name': 'Aye Aye'}, {'city': 'Yangon'})
print(getdata["name"]) # Aye Aye
print(getdata["city"]) # Yangon
# 15CM

# array (from array module)
from array import array

myarrs = array('i',[10,20,30,40,20])
print(myarrs)

getlength = len(myarrs)
print(getlength) 

print(myarrs[0])
print(myarrs[2])

myarrs.append(50)
print(myarrs)

print(myarrs.index(50)) # 5

print(myarrs.count(20)) # 2

myarrs.insert(1,100)
print(myarrs) # array('i', [10, 100, 20, 30, 40, 20, 50])

myarrs.remove(30)
print(myarrs) # array('i', [10, 100, 20, 40, 20, 50])

for value in myarrs:
     print(value)

myarrs.reverse()
print(myarrs) #array('i', [50, 20, 40, 20, 100, 10])

#=> queue (from queue module)
from queue import Queue 

qone = Queue() # Queue(0) meain infinite size
qone.put(400)
qone.put(100)
qone.put(300)

print(qone.get()) # 400 get after remove data
print(qone.get()) # 100
print(qone.get()) # 300



# What is deque?
# A deque (short for "double-ended queue") is a data structure where you can:
# Add items to both the front and back.
# Remove items from both the front and back.

# Feature	               Deque	               List
# Addition at Front	     Very fast (appendleft())	Slow (requires shifting all elements).
# Removal from Front	     Very fast (popleft())	Slow (requires shifting all elements).
# Addition at Back	     Fast (append())	     Fast (append()).
# Removal from Back	     Fast (pop())	          Fast (pop()).
# Random Access (Indexing)	Not efficient; requires iterating to the index.	Very fast (list[index]).





# What is defaultdict?
# The defaultdict is a specialized dictionary class in Python, available in the collections module. Unlike a regular dictionary, it automatically initializes a default value for non-existent keys when accessed. This eliminates the need to manually check for the presence of a key before assigning a value.

# How defaultdict Works
# When you create a defaultdict, you specify a default factory function (e.g., list, int, str).
# If a key is accessed that doesn’t exist in the dictionary:
# Instead of raising a KeyError, the defaultdict automatically creates the key with the default value provided by the factory function.
# {
#     'fruits': ['apple', 'mango', 'banana'],
#     'colors': ['orange']
# }
# How It Works
# defaultdict(list):

# Creates a dictionary where each new key will have a default value of an empty list.
# items['fruits'].append('apple'):

# Since the key 'fruits' doesn’t exist, the defaultdict creates it and assigns it an empty list as the default value.
# 'apple' is appended to the list associated with the 'fruits' key.


# What is OrderedDict?
# An OrderedDict is a specialized dictionary class from Python’s collections module. It preserves the order of the items as they are added to the dictionary, unlike a regular dictionary in Python versions prior to 3.7, which did not guarantee order.
# Advantages of OrderedDict
# Guaranteed Order:

# Essential for older Python versions (<3.7) where dict does not guarantee insertion order.
# Reordering Items:

# Methods like move_to_end and popitem make it easy to rearrange items.
# Consistency:

# Useful in scenarios where order consistency matters, such as:
# Serializing data (e.g., JSON).
# Writing configurations.
# Creating LRU (Least Recently Used) caches.


# What is a Queue?
# A Queue is a data structure that follows the FIFO (First In, First Out) principle. This means the first element added to the queue is the first one to be removed. Think of a queue like a line of people waiting for a service: the person at the front gets served first, and new arrivals join at the back.

# Key Characteristics of a Queue
# FIFO Behavior:

# The first element inserted is the first to be removed.
# Two Main Operations:

# Enqueue: Add an element to the back of the queue.
# Dequeue: Remove an element from the front of the queue.
# Fixed or Dynamic Size:

# Queues can be implemented with a fixed size or dynamically grow/shrink as needed.