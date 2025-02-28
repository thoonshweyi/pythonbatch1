# => map()

# syntax
# map(function,iterable)


numbers = [1,2,3,4,5,6,7,8,9,10]

def square(num):
     return num ** 2

result = map(square,numbers)
print(list(result)) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

result2 = map(lambda x:x ** 2,numbers)
print(list(result2)) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter() vs map()
result3 = list(filter(lambda x: x%2 == 0,numbers))
print(list(result3)) # [2, 4, 6, 8, 10]

result3 = list(map(lambda x: x%2 == 0,numbers))
print(list(result3)) # [False, True, False, True, False, True, False, True, False, True]

# converting string to upper, lower, capitalize
backend = ["php","Nodejs","PYTHON"]

result4 = list(map(str.upper,backend))
print(list(result4)) # ['PHP', 'NODEJS', 'PYTHON']

result5 = list(map(str.lower,backend))
print(list(result5)) # ['php', 'nodejs', 'python']

result6 = list(map(str.casefold,backend))
print(list(result6)) # ['php', 'nodejs', 'python']

result7 = list(map(str.capitalize,backend))
print(list(result7)) # ['Php', 'Nodejs', 'Python']

# nested list
nestedlist = [[10,20],[30,40],[50,60]]
result8 = list(map(lambda x: x[0]+x[1],nestedlist))
print(result8) # [30, 70, 110]


# witha tuple

tuples = (10,15,20,25,30,35,40,45,50)
result9 = tuple(map(lambda x : x/10,tuples))
print(result9) # (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)

# with Dictionary 
students = {"Su Su":18,"Aung Aung":20,"Yamin":16,"Nilar":19}
result10 = dict(map(lambda student: (student[0],student[1]* 2) ,students.items()))
print(result10) # {'Su Su': 36, 'Aung Aung': 40, 'Yamin': 32, 'Nilar': 38}

# with set 

numberset = {1,2,3,4,5,6,7,8,9,10}
result7 = set(map(lambda x: x * 2, numberset))
print(result7) # {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

# multi iterables
num1 = [1,2,3]
num2 = [4,5,6]
result8 = list(map(lambda x,y:x+y,num1,num2))
print(result8) # [5, 7, 9]