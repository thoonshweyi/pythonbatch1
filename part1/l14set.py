# =>Data Containers

# list
mylist = [1,2,3,4,5]
print(type(mylist)) #<class 'list'>

# tuple
mytuple = (1,2,3,4,5)
print(type(mytuple)) #<class 'tuple'>

# dict
mydict = {"a":1,"b":2,"c":3}
print(type(mydict)) #<class 'dict'>

# set
myset = {1,2,3,4,5}
print(myset) #{1, 2, 3, 4, 5}
print(type(myset)) #<class 'set'>

dict1 = {}
print(type(dict1)) #<class 'dict'>

set1 = {}
print(type(set1)) #<class 'dict'>

# create an empty set 
set2 = set()
print(type(set2)) #<class 'set'>

colors = {'red','green','blue','white','black'}
print(colors)
# {'green', 'blue', 'black', 'red', 'white'}
# {'red', 'white', 'black', 'green', 'blue'}

for color in colors:
     print(color)

print('green' in colors) #True
print('steelblue' in colors) #False


# Adding a single Element
fruits = {"apple","orange"}
print(fruits) #{'apple', 'orange'}

fruits.add("cherry")
print(fruits) #{'cherry', 'orange', 'apple'}

# Adding Multiple Element []
fruits.update(["mango","grape"])
print(fruits) #{'mango', 'orange', 'grape', 'apple', 'cherry'}

# Remove Elements
# fruits.remove("red") #Error (if no element exists ! will show an error)
fruits.remove("orange") 
print(fruits) #{'grape', 'apple', 'mango', 'cherry'}

# Remove Elements (using discard())
fruits.discard('red') #if no element exiss ! no error

fruits.discard('apple') #{'mango', 'grape', 'cherry'}
print(fruits)

# Clear Elements
fruits.clear() 
print(fruits) # set()

# Frozenset (Immutable of set)
fornumbers = frozenset([10,20,30,40,50])
# fornumbers.add(50) #error
# fornumbers.remove(40) #error
print(fornumbers) #frozenset({40, 10, 50, 20, 30})
print(20 in fornumbers) #True
print(60 in fornumbers) #False

set3 = {1,2,3,6,7}
set4 = {3,4,6,5}

# Union Combines ( | )
print(set3 | set4) #{1, 2, 3, 4, 5, 6,7}
print(set3.union(set4)) #{1, 2, 3, 4, 5, 6,7}



# Intersection ( & )
print(set3 & set4) #{3, 6}
print(set3.intersction(set4)) #{3, 6}


# Difference (-)
print(set3 - set4) #{1, 2, 7}
print(set3.difference(set4)) #{1, 2, 7}

print(set4 - set3) #{4, 5}
print(set4.difference(set3)) #{4, 5}


#Symmetric Difference (^)
print(set3 ^ set4) #{1, 2, 4, 5, 7}
print(set3.symmetric_difference(set4)) #{1, 2, 4, 5, 7}

print(set4 ^ set3) #{1, 2, 4, 5, 7}
print(set4.symmetric_difference(set3)) #{1, 2, 4, 5, 7}

# 1ST

# => set comprehension
# {expression for item in iterable condition}
                    # 0 to 4
squares = { x**2 for x  in range(5)}
print(squares) # {0, 1, 4, 9, 16}

# 0 ** 2 = 0
# 1 ** 2 = 1
# 2 ** 2 = 4
# 3 ** 2 = 9
# 4 ** 2 = 16

evens = { x for x in range(10) if x%2 == 0}
print(evens) # {0, 2, 4, 6, 8}

uniqchars = { char for char in "hello world" }
print(uniqchars) # {' ', 'r', 'o', 'e', 'd', 'l', 'h', 'w'}

numbers = [1,2,2,3,4,7,5,7]
uniqnumbers = {x for x in numbers}
print(uniqnumbers) # {1, 2, 3, 4, 5, 7}

# => Nested Loops in set comprehension 
couplenums = { (x,y) for x in range(3) for y in range(2)}
print(couplenums) #{(0, 1), (2, 1), (0, 0), (1, 1), (2, 0), (1, 0)}

# x takes value to 0 to 2
# y takes value to 0 to 1
# x=0 y=0      (0,0)
# x=0 y=1      (0,1)
# x=1 y=0      (1,0)
# x=1 y=1      (1,1)
# x=2 y=0      (2,0)
# x=2 y=1      (2,1)

# It is like, the target value is printed at the innermost part of the loop
# for x in range(3) 
#    for y in range(2)
#         print(x,y)

#=> Generator Function

def genfun():
     yield 1
     yield 2
     yield 3

print(genfun()) # <generator object genfun at 0x00000223F8974930>
print(list(genfun())) # [1, 2, 3]

for value in genfun():
     print(value) # 1 2 3




# Union Operation (|)
     # Definition:

     # The union of two sets combines all unique elements from both sets into a single set.
     # The | operator is a shorthand for the .union() method.
     # Behavior:

     # It removes any duplicate elements, ensuring each element appears only once in the result.
     # The resulting set includes all elements that are in either set or in both sets.
     # Key Points to Remember:
     # The | operator works only with sets.
     # If either operand is not a set, it will raise a TypeError.
     # Union operation does not modify the original sets; it creates a new set as the result.


# . Sets Are Unordered
     # A set in Python is implemented as a hash table.
     # The position of elements in a set is determined by their hash values, not by their insertion order.
     # Hash values are used for fast lookup and comparison, and the arrangement can change depending on the set's internal state.
     # Key Point: Numbers vs Strings
     # Numbers: Hash values often correspond to the numbers themselves, so sets of numbers appear sorted.
     # Strings: Hash values are not tied to their order, so the arrangement appears random.


# Intersection (&) in Python Sets
# The intersection operation between two sets in Python returns a new set containing only the elements that are present in both sets.

# The & operator is used to perform this operation


# Difference (-) in Python Sets
# The difference operation between two sets returns a new set containing elements that are in the first set but not in the second set. It effectively "removes" all elements from the first set that are also present in the second set.

# Symmetric Difference (^) in Python Sets
# The symmetric difference operation between two sets returns a new set containing elements that are in either of the sets, but not in both. It effectively excludes the common elements from the union of the two sets.


# Set Comprehension in Python
# Set comprehension is a concise and elegant way to create sets in Python, similar to list comprehensions but for sets. It allows you to generate sets based on an expression, an iterable, and optional conditions, all in a single line.
#    Syntax of Set Comprehension
     # {expression for item in iterable if condition}
     # expression: This is the value to include in the set. It can involve calculations or transformations of the items in the iterable.
     # for item in iterable: Iterates over the elements of an iterable (like a list, range, etc.).
     # if condition (optional): Filters elements; only elements satisfying the condition are included in the set.