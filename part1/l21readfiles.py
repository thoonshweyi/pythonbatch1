# => Open File 
# mode
# 'r' = Read (default)
# 'w' = Write
# 'a' = Append

# syntax
# open('filename.txt',mode)

# => Read File
# read()       = Read the entire file
# readline()   = Read on line at a time
# readlines()  = Read all lines into a list


# Method 1 ,read(),(with statement), Read all content at once, Not memory-efficient for large files

with open('files/file1.txt','r') as file:
     # print(file) #<_io.TextIOWrapper name='files/file1.txt' mode='r' encoding='cp1252'>

     getcontent = file.read()
     print(getcontent)

# => File Encoding
print("\n Method 1, read()")

with open("files/file1.txt",'r',encoding='UTF-8') as file:
     # print(file) # <_io.TextIOWrapper name='files/file1.txt' mode='r' encoding='UTF-8'>
     getcontent = file.read()
     print(getcontent)


# => Read Specific Number of characters
print("\n Read Specific Number of characters")

with open("files/file1.txt",'r',encoding='UTF-8') as file:
     getcontent = file.read(10) # Reads the first 10 characters
     print(getcontent) # Hello Worl


# => Method 2 using strip(), Read line by line (One line at a time, Efficient for large file)
print("\n Method 2, Using strip()")
with open("files/file1.txt",'r') as file:
     for line in file:
          # print(line)
          print(line.strip()) # .strip() removes extra newline characters

# Method, readline(), Read line by line
print("\n Method 3, Using strip()")
with open("files/file1.txt",'r') as file:
    lines = file.readline()
    print(lines)

    while lines:
         print(lines.strip())
         lines = file.readline()

# Method 4, readlines(), Read all line, (All lines at once, can use a lot of memory for large files)

print("\n Method 4, readline()")
with open("files/file1.txt",'r') as file:
     lines = file.readlines()
     print(lines) # ['Hello World!\n', 'This is Python Batch 1 zoom class.\n', 'How to read file in python programming language.']
     for line in lines:
          print(line.strip())

# => Handling Exceptions
# (i) FileNotFoundError
# (ii) PermissionError
# (iii) IOError
print("\n Handling Exceptions")

try:
     with open('files/file1.txt','r') as file:
          getcontent = file.read()
          print(getcontent)
except FileNotFoundError:
     print("Your file does not exist.")
except PermissionError:
     print("You do not have the necessary permissions")
except IOError as err:
     print(f"An IO error: {err}")
finally:
     print("program Completed")


# Why Does It Still Print Line by Line?
# Each iteration reads a new line from the file.
# .strip() removes extra spaces and \n from the line.
# print(line.strip()) prints the cleaned-up line but still moves to the next line because print() adds \n by default.