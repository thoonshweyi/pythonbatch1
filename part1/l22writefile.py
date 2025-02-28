# => Write a File 

# sudo chmod 777 -R files/
# mode
# 'r' = Read (default)
# 'w' = Write
# 'a' = Append

# syntax
# open('filename.txt',mode)

# => Read File
# write()       
# writelines()   


# Method 1 ,write()
print("\n Method 1, write()")

file = open('files/file2.txt','w')
file.write("Hello World!")
file.close()

# => Method 2, writelines()
print("\n Method 2, writelines()")
lines = ["Hello World! \n","This is Python Batch 1 zoom class.\n","How to read file in python programming language."]
file = open("files/file3.txt","w")
file.writelines(lines)
file.close()

# Using with statement
print("\n Using with statement")
with open("files/file4.txt","w") as file:
     file.write("Hello Sir! \n")
     file.write("This is Python Batch 1 zoom class. \n")
     file.write("How to read file in python programming language. \n")



# =>Append to a file
print("\n Append to a file")

with open("files/file5.txt","a") as file:
     file.write("\n This line is appended to the file")


print("\n with variable")
name = "Yu Yu"
age = 27
with open("files/file6.txt","w") as file:
     file.write(f"My name is {name} and i am {age} years old.\n")

# =>Error Handling
print("\n Error Handling")

try:
     with open("files/file7.txt","w") as file:
          file.write("This is Python Batch 1 zoom class. \n")
except IOError as err: # General case
     print(f"An IO Error: {err}")
finally:
     print("Program Completed")


# 1. with open(...) (Context Manager Approach)
#  Advantages of with open(...):
# Automatic Resource Management – The file closes automatically after exiting the with block, even if an error occurs.
# No Need for file.close() – Python handles closing the file for you.
# Prevents File Corruption – If the script crashes before file.close(), this method ensures the file is properly closed.
# 🚀 When to Use with open(...)?
# Recommended for reading, writing, or appending files.
# Useful when handling exceptions automatically.

# 2. Declaring File Variable Manually (file = open(...))
# Disadvantages of Manually Opening Files
# You must close the file manually (file.close()). If you forget, it can cause memory leaks or file corruption.
# If an error occurs before file.close(), the file remains open.
# More lines of code compared to with open(...).
# ✔ When to Use file = open(...)?
# When you explicitly need to keep the file open for multiple operations.
# If handling files outside a block structure.

# Key Differences Table
# Feature	                         with open(...) (Context Manager)	file = open(...) (Manual)
# Closes file automatically?	     ✅ Yes	                         ❌ No (must use file.close())
# Handles exceptions?	          ✅ Yes	                         ❌ No
# Prevents memory leaks?	          ✅ Yes	                         ❌ No
# Ease of use?	                    ✅ Easy	                         ❌ Requires manual handling
# Good for large file handling?	✅ Yes	                         ❌ No (risk of open file leak)




# writelines() writes multiple lines at once but does not add \n automatically.
# If you want line breaks, you must include \n manually.
# Use "w" mode to overwrite or "a" mode to append.
# It is faster than multiple write() calls when writing many lines.

# Comparison: write() vs writelines()
# Method	          What it does	                    Adds \n automatically?	Input type
# write()	          Writes a single string to the file	❌ No	                    String (str)
# writelines()	     Writes multiple lines at once	     ❌ No	                    List of strings (list[str])


# Why Doesn’t Each write() Overwrite the Previous Line?
# The write() function does not reset the cursor to the beginning of the file each time it runs.
# Instead, it keeps appending sequentially within the same file session.
# 🚀 Key Rule:
# "w" mode only clears the file at the time of opening.
# Subsequent write() calls continue from the last cursor position until the file is closed.