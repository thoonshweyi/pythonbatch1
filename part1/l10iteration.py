# =>for in loop
# Iteration a list
colors = ["red","green","blue"]

for color in colors:
     print(color)


# Iteration a string
message = "Hello World"
print(len(message))

for msg in message:
     print(msg)

# Iteration a dictionary
students = {"name":"Su Su","age":20,"city":"Mandalay"}

print(students)
print(students.items()) #dict_items([('name', 'Su Su'), ('age', 20), ('city', 'Mandalay')])

for key in students:
     print(key,students[key])

for key,value in students.items():
     print(key,"=",value)

# =>range() in for in loop 
for x in range(10):
     print(x) # 0 to 9

print(f"Outside x value is {x}") #Outside x value is 9

for y in range(1,5):
     print(y) # 1 to 4

print(f"Outside y value is {y}") #Outside y value is 4

for p in range(1,10,2):
     print(p) # 1 3 5 7 9

print(f"Outside p value is {p}") #Outside p value is 9


# =>break and continue
for i in range(10):
     if i == 5:
          break # Exit the loop if i is 5
     print(i) # 0 to 4
print(f"Outside i value is {i}") #Outside i value is 5


for q in range(10):
     if q == 5:
          continue # Skip even number 5
     print(q) # 0 1 2 3 4 6 7 8 9
print(f"Outside q value is {q}") #Outside i value is 9


for j in range(10):
     if j % 2 == 0:
          continue 
     print(j) # 1 3 5 7 9
print(f"Outside j value is {j}") #Outside j value is 9

# Nested Loops 

staffs = [
     ["aung aung","kyaw kyaw","zaw zaw"],
     ["su su","nu nu","yu yu"],
     ['thidar','nilar','muyar']
]

# for staff in staffs:
#      for people in staff:
#           print(people)

# for staff in staffs:
#      for people in staff:
#           print(people)
#      print()

# for staff in staffs:
#      for people in staff:
#           print(people,end=" ") # aung aung kyaw kyaw zaw zaw su su nu nu yu yu thidar nilar muyar

for staff in staffs:
     for people in staff:
          print(people,end=" ") # aung aung kyaw kyaw zaw zaw su su nu nu yu yu thidar nilar muyar
     print()

# => while loop 
idx = 0

while idx < 10:
     print(f"Index : {idx}")
     idx += 1

print(f"Outside idx value is {idx}") #Outside idx value is 10


count = 0

while count < 10:
     count += 1
     print(f"Index : {count}") # 1 to 10

print(f"Outside count value is {count}") #Outside j value is 10


paints = ["red","green","blue"]
print(paints) #
print(enumerate(paints)) #<enumerate object at 0x000002A71CD10450>

for index,paint in enumerate(paints):
     print(index,paint)

index = 0
while index < len(paints):
     print(index, paints[index])
     index += 1

# break
# while True:
#      username = input("Enter username = ")
#      if(username == 'aungaung'):
#           break
#      else:
#           continue


initnum = False 
while not initnum:
     luckynum = input("Enter your lucky number = ")
     if(luckynum.isdigit() and int(luckynum) > 0):
          initnum = True 
          print(f"Your lucky number is {luckynum}")
     else: 
          print("Invalid Number")


# Iterating Over Key-Value Pairs Using .items()
#    The .items() method returns a view object containing key-value pairs as tuples. 
#    You can unpack these pairs into two variables while iterating.
#    .items() Method in Python
#    The .items() method is a dictionary method that returns a view object. 
#    This view object contains key-value pairs as tuples, which can be iterated over or converted to other data structures.
#    Why Use .items()?
#    It’s particularly useful when you need to access both keys and values at the same time while iterating through a dictionary.

# Why Iterating Over a Dictionary Only Gets Keys by Default?
# Default Behavior
# When you iterate directly over a dictionary, only the keys are returned by default:

# end: A string to append after the content is printed.
# Default: '\n' (new line).
# Custom: Any string or empty string ("").


# Using enumerate() with list()
# The enumerate() object can be converted into a list of tuples.
# enumerate(paints) automatically pairs each item in the list with its index.
# The index and paint variables unpack the tuple (index, item) returned by enumerate().