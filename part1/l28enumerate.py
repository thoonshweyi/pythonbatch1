# enumerate() 

colors = ["red","green","blue"]

for color in colors:
     print(color)

for index,color in enumerate(colors):
     print(index,color) # 0 red 1 green 2 blue


numbers = [10,20,30,40]
for idx,value in enumerate(numbers):
     numbers[idx] = value * 2
print(numbers) # [20, 40, 60, 80]

colors = ["red","green","blue","black","white"]
for idx,color in enumerate(colors):
     if color == "black":
          print(f"black color is exists.")

# = custom start index
for index,color in enumerate(colors,start=10):
     print(f"Index {index} : {color}")

message = "Hello World"
for index,msg in enumerate(message):
     print(index,msg)


colours = ["Red","Green","Blue"]
colourlist = list(enumerate(colours,100))

print(colourlist)