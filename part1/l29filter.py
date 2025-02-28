# filter

# syntax 
# filter(function,iterable)

numbers = [1,2,3,4,5,6,7,8,9,10]

def iseven(num):
     return num%2 == 0

result = filter(iseven,numbers)
print(list(result)) # [2, 4, 6, 8, 10]

result2 = filter(lambda x: x % 2 == 0,numbers)
print(result2) # <filter object at 0x000001C5558F6230>
print(list(result2)) # [2, 4, 6, 8, 10]

# filter more than 5 letters 
backend = ["php","nodejs","python"]
result3 = list(filter(lambda letter: len(letter) > 5,backend))
print(result3) # ['nodejs', 'python']

# with Tuple
tuples = (10,15,20,25,30,35,40,45,50)
result4 = tuple(filter(lambda x : x>30,tuples))
print(result4) # (35, 40, 45, 50)

# with Dictionary 
students = {"Su Su":18,"Aung Aung":20,"Yamin":16,"Nilar":19}
print(students.items()) # dict_items([('Su Su', 18), ('Aung Aung', 20), ('Yamin', 16), ('Nilar', 19)])

result5 = dict(filter(lambda student: student[1] > 18,students.items()))
print(result5) # {'Aung Aung': 20, 'Nilar': 19}

# with set 
numberset = {1,2,3,4,5,6,7,8,9,10}
result6 = set(filter(lambda x: x % 2 == 0, numberset))
print(result6) # {2, 4, 6, 8, 10}

# remove none value
datas = [True,1,None,2,'',False,3,None,4,"",True,5]
result7 = list(filter(lambda x: x is not None and x != '',datas))
print(result7) # [True, 1, 2, False, 3, 4, True, 5]

