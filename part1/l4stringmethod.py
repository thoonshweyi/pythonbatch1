name = "aung kyaw"
print(name) #
print(name[0]) # a
print(name[3]) # g
print(name[8]) # w
print(name[-1]) # w
print(name[-2]) # a
print(name[-8]) # u

# start:end:step
print(name[0:1]) # a
print(name[0:2]) # au
print(name[0:3]) # aun
print(name[0:4]) # aung

print(name[1:4]) # ung
print(name[1:7]) # ung ky
print(name[0:9]) # aung kyaw

print(name[0:9:1]) # aung kyaw
print(name[0:9:2]) # an yw
print(name[0:9:3]) # agy
# count step from the selected index and stop after forwarded

fullname = name #aung kyaw
fullname = name[:] #aung kyaw
fullname = name[0:4] #aung
fullname = name[::-1] #wayk gnua
print(fullname) 

getlength = len(name)
print(getlength) #9

test = "hello friend"
print(test.upper()) #HELLO FRIEND

print(test.capitalize()) #Hello friend
print(test.title()) #Hello Friend

task = "HAVE TO GO"
print(task.lower()) #have to go
print(task.casefold()) #have to go

todo = "Have To Shop"
print(todo.swapcase()) #hAVE tO sHOP

hifi = "    hello friend    "
print(hifi) #   hello friend
print(hifi.strip()) #hello friend
print(hifi.lstrip()) #hello friend
print(hifi.rstrip()) #   hello friend


greet = "hello friend"
print(greet.replace('friend','sir')) #hello sir
print(greet.replace('Friend','sir')) #hello friend


print(greet.startswith('h')) #True
print(greet.startswith('he')) #True
print(greet.startswith('H')) #False
print(greet.startswith('He')) #False


print(greet.endswith('nd')) #True
print(greet.endswith('friend')) #True
print(greet.endswith('Friend')) #False


mobile = "OPPO"
print(mobile.isupper()) #True
print(mobile.islower())#False

num1 = 528
num2 = '1500'
num3 = 'ten'

####
####

# print(num1.isdigit()) # error cuz of isdigit() can check only for string
print(str(num1).isdigit()) # True
print(num2.isdigit()) #True
print(num3.isdigit()) #False

print(num2.isalpha()) #False
print(num3.isalpha()) #True

print(num2.isnumeric()) #True
print(num3.isnumeric()) #False

print(num2.isalnum()) #True
print(num3.isalnum()) #True

num4 = "number ten"
num5 = "hay!"
print(num4.isalnum()) # False (cuz of space)
print(num5.isalnum()) # False (cuz of !)

middlename = " "
print(middlename.isspace()) #True #check only for single space character

nickname = "Aung Moe"
print(nickname.isspace()) #False
print(nickname.istitle()) #True


sayhi = "Hi My Friend"
print(sayhi.split()) # ['Hi', 'My', 'Friend']

color = 'red,green,blue,white,black'
print(color.rsplit()) # ['red,green,blue,white,black']

sayhello = "Hello\nFriend"
print(sayhello.splitlines()) #['Hello', 'Friend']

####
sayhifi = "Hello Friend Mr.Maung"
print(sayhifi.partition(' ')) #('Hello', ' ', 'Friend Mr.Maung')
print(sayhifi.partition('.')) #('Hello Friend Mr', '.', 'Maung')


post = "Reads"
print(post.ljust(10,'-'))     #Read------
print(post.rjust(10,'-'))     #------Read
print(post.center(10,'-'))    #---Read---         #--Reads--- (bias right if center conflit)


city = "Hello {}"
print(city.format("Mandalay")) #Hello Mandalay

country = "Hello {} {}"
print(country.format("Mandalay","Myanmar")) #Hello Mandalay Myanmar

print("Hello my {}.are you {}!".format('friend',"Aung Aung"))


val1 = "sister"
val2 = "Su Su"
print("Hello my {}.are you {}!".format(val1,val2))

#dictionary
student = {"name":"Su Su"}
sayname = "Dear, {name}"

print(sayname.format_map(student)) #Dear, Su Su

message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy Text ever since the 1500s lorem"
countoflorem = message.count('Lorem')
print(countoflorem) #2

countoftext = message.count('text')
print(countoftext) #1



# What Does [:] Mean in Python?
# The [:] syntax is a way of slicing a sequence in Python. This can apply to strings, lists, tuples, etc. Here's what it means:

# name[:]: This creates a new copy of the entire content of the variable name (from start to end).
# No start, end, or step values are specified, so it defaults to:
# start = 0: Beginning of the string.
# end = len(name): End of the string.
# step = 1: Every character is included.


# isdigit() Method
# Checks if all characters in the string are digits (0–9).
# Works only with decimal digits and doesn't recognize special numeric characters like fractions or Roman numerals.
# Usage Example:
# print("12345".isdigit())  # Output: True
# print("123.45".isdigit())  # Output: False (contains a period)
# print("²".isdigit())       # Output: True (superscript 2 is a digit)
# print("⅕".isdigit())       # Output: False (fraction is not a digit)
# Key Points:
# Only considers decimal digits and some special numeric characters (like superscripts).
# It returns False if the string contains anything other than simple digits (like -, ., or fractions).

#  isnumeric() Method
# Checks if all characters in the string represent numeric values, including more than just digits.
# Recognizes fractions, Roman numerals, and Unicode numeric characters.
# Usage Example:
# python
# Copy code
# print("12345".isnumeric())  # Output: True
# print("123.45".isnumeric())  # Output: False (contains a period)
# print("²".isnumeric())       # Output: True (superscript 2 is numeric)
# print("⅕".isnumeric())       # Output: True (fraction ⅕ is numeric)
# print("V".isnumeric())       # Output: False (V is not numeric; it's a Roman numeral symbol)
# Key Points:
# It recognizes fractional numbers and other Unicode numeric characters (like ⅕).
# Returns False for decimal points (.) or negative signs (-), just like isdigit().


# Method	     Checks For	     Example "Hello123"	Example "Hello!"	Example "123"
# isalpha()	Only letters	     False	          False	          False
# isalnum()	Letters or digits	True	               False	          True


# Method	          Description	                         Example Input	          Example Output
# split()	          Splits from left using a separator	     "a b c".split()	     ['a', 'b', 'c']
# rsplit()	     Splits from right using a separator	"a,b,c".rsplit(",", 1)	['a,b', 'c']
# splitlines()	     Splits at line breaks (\n, \r\n, \r)	"a\nb\nc".splitlines()	['a', 'b', 'c']

# split()
# The split() method splits a string into a list of substrings using a delimiter (separator). 
# By default, it splits by whitespace (spaces, tabs, or newlines)

# rsplit()
# The rsplit() method works similarly to split(), but it starts splitting from the right side of the string.
# Useful when you only care about the last few parts of a string.(e.g., get the last part of a URL)

# splitlines()
# The splitlines() method splits a string at line breaks (\n, \r\n, or \r). It is often used to process multi-line strings.
# Useful for handling multi-line text files.

# The partition() function in Python is used to split a string into three parts:
# Before the separator
# The separator itself
# After the separator
# If the separator is not found, the entire string is placed in the first part, with the other two parts being empty strings ('')

# The format() function in Python is used to insert values into strings by formatting them in a readable or structured way. 
# It offers a clean and flexible way to embed variables directly into strings, making code easier to read and maintain.
# Feature	               Example	                              Output
# Basic Formatting	     "{} {}".format("Hello", "World")	     Hello World
# Positional Arguments	"{1} {0}".format("World", "Hello")	     Hello World
# Named Placeholders	"{name}".format(name="Alice")	          Alice

# The format_map() function in Python is similar to format(), but it allows you to directly substitute values from a dictionary into a string. 
# It’s a concise way to embed data stored in dictionaries into strings.
# Instead of passing individual values like in format(), you provide a dictionary.
# The keys of the dictionary match the placeholders inside the string.