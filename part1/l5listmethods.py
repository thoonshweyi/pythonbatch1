names = ["aung aung","maung maung","su su","yu yu","nandar"]
print(names) # ['aung aung', 'maung maung', 'su su', 'yu yu', 'nandar']

mixeds = [1500,'hello',123.6,True,'world',False]
print(mixeds) # [1500, 'hello', 123.6, True, 'world', False]

print(mixeds[0]) # 1500
print(mixeds[3]) # True
print(mixeds[-1]) # False
print(mixeds[-2]) # world

print(mixeds[0:1]) # [1500]
print(mixeds[0:2]) # [1500, 'hello']
print(mixeds[1:3]) # ['hello', 123.6]
print(mixeds[0:6]) # [1500, 'hello', 123.6, True, 'world', False]

print(mixeds[0:6:2]) # [1500, 123.6, 'world']
print(mixeds[0:6:3]) # [1500, True]


mix2 = mixeds
mix2 = mixeds[:] #[1500, 'hello', 123.6, True, 'world', False]
mix2 = mixeds[0:4] #[1500, 'hello', 123.6, True]
mix2 = mixeds[::-1] #[False, 'world', True, 123.6, 'hello', 1500]
print(mix2) #[1500, 'hello', 123.6, True, 'world', False]


getlength = len(names)
print(getlength) #5

colors = ['red','green','blue']
print(colors) #['red', 'green', 'blue']

colors[0] = 'pink'
print(colors) #['pink', 'green', 'blue']

# colors[3] = 'silver' #error (list assignment index out of range)
# print(colors)

# add data from end(single)
colors.append('white') #['pink', 'green', 'blue', 'white']
# colors.append('black','violet') #error(list.append() takes exactly one argument (2 given))
print(colors) 

#add data from end(multi)
colors.extend(['gold']) #['pink', 'green', 'blue', 'white', 'gold']
colors.extend(['black','violet']) #['pink', 'green', 'blue', 'white', 'gold', 'black', 'violet']
print(colors) 

colors.insert(0,'steelblue')
print(colors) #['steelblue', 'pink', 'green', 'blue', 'white', 'gold', 'black', 'violet']
# first param is position to insert

# remove value and index
colors.remove('green') #['steelblue', 'pink', 'blue', 'white', 'gold', 'black', 'violet']
print(colors)

# remove from end value and index
colors.pop()
print(colors) #['steelblue', 'pink', 'blue', 'white', 'gold', 'black']

# remove value and index
del colors[1] #['steelblue', 'blue', 'white', 'gold', 'black']
del colors[1:3] #['steelblue', 'gold', 'black']
print(colors)

vals = [1,2,3,4,5]
print(f"Before clear values {vals}") #Before clear values [1, 2, 3, 4, 5]
vals.clear()
print(f"After clear values {vals}") #After clear values []

boys = ['aung aung','zaw zaw','kyaw kyaw','hein min','yea lay','min khant']
boys.sort() #['aung aung', 'hein min', 'kyaw kyaw', 'min khant', 'yea lay', 'zaw zaw']
print(boys)


boys.reverse() 
print(boys) #['zaw zaw', 'yea lay', 'min khant', 'kyaw kyaw', 'hein min', 'aung aung']
# indirect z-a

nums = [10,115,11,1,50,30,75,25,65,90,110]
nums.sort()
print(nums) #[1, 10, 11, 25, 30, 50, 65, 75, 90, 110, 115]
# number can be sorted directly without using callback function like javascript

nums.reverse()
print(nums) #[115, 110, 90, 75, 65, 50, 30, 25, 11, 10, 1]
# indirect max-min

ages = [18,25,30,18,30,25,25,20,18,25]
countof18 = ages.count(18)
print(countof18) #3

countof20 = ages.count(20)
print(countof20) #1

countof25 = ages.count(25)
print(countof25) #4

print(ages.index(20)) #7
print(ages.index(30)) #2


# nested list 
numbers = [[1,2,3],[40,50,60],[700,800,900]]
print(len(numbers)) #3
print(numbers[0]) #[1, 2, 3]
print(numbers[1]) #[40, 50, 60]
print(numbers[2]) #[700, 800, 900]
# print(numbers[3]) # error
print(numbers[2][0]) #700
print(numbers[2][2]) #900


numbers.append([1000,2000]) #[[1, 2, 3], [40, 50, 60], [700, 800, 900], [1000, 2000]]
print(numbers)

numbers.pop()
print(numbers) #[[1, 2, 3], [40, 50, 60], [700, 800, 900]]

numbers.pop(1)
print(numbers) #[[1, 2, 3], [700, 800, 900]]

# List Unpacking
greeting = ['Hello','Su Su']
print(" ".join(greeting)) #Hello Su Su
print("-".join(greeting)) #Hello-Su Su


print(greeting[0]) #Hello
print(greeting[1]) #Su Su


val1,val2 = greeting 
print(val1)#Hello
print(val2)#Hello


# list()
greeting = "Hello Sir"
print(list(greeting)) # ['H', 'e', 'l', 'l', 'o', ' ', 'S', 'i', 'r']

# => zip(), iterables (such as lists, tuples,string)
arrone = ["10","20","30"]
arrtwo = ["hi","hello","bye"]

createzip = zip(arrone,arrtwo)
print(createzip) #<zip object at 0x000002821D85ACC0>

converttolist = list(createzip)
print(converttolist) # [('10', 'hi'), ('20', 'hello'), ('30', 'bye')]




# The append() method adds a single element to the end of the list
# The extend() method adds all elements from an iterable (like another list, tuple, or set) to the end of the list, unpacking them.
# Key Differences Between append() and extend()
# Feature	          append()	                                   extend()
# Purpose	Adds      one element to the end	               Adds multiple elements (unpacked)
# Works with	     Any data type (string, list, etc.)	     Any iterable (list, string, set, etc.)
# Example with      List	lst.append([1, 2]) → [[1, 2]]	     lst.extend([1, 2]) → [1, 2]



# How insert() Works
# The new element is placed at the specified index, and all the existing elements from that position onward are shifted to the right.
# If the index is greater than the list’s length, the element is added to the end.
# If the index is negative, it starts counting from the end of the list.


# How remove() Works
# It searches the list from left to right for the first occurrence of the specified element.
# If it finds the element, it removes it.
# If the element is not found, it raises a ValueError.


# How pop() Works
# It removes the element at the given index.
# It returns the removed element so it can be used later if needed.
# If no index is given, it removes and returns the last element.


# How del Works
# Deletes a variable, list element, or dictionary key.
# Does not return any value.
# If you try to access a deleted object, it raises a NameError or KeyError depending on the context.


# The clear() function in Python is used to remove all elements from a list or dictionary, leaving it empty. This operation does not delete the object itself but clears its contents.

