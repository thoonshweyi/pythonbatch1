import os
import time
# => get current working directory
print(os.getcwd())  #D:\datalandcourses\pythonbatch1\part3

# => change directory
# os.chdir("..")
# print(os.getcwd()) # D:\datalandcourses\pythonbatch1

# => list files and directories
print(os.listdir()) # ['.git', 'part1', 'part2', 'part3']
# list everything in the current dir

# => create a new directory (single)
# os.mkdir("newfolder")

# => create a new directory (nested)
# os.makedirs("folder1/folder2/folder3/folder4",exist_ok=True)

# => Rename a file
# with open("oldname.txt","w") as file:
#      file.write("Welcome Mandalay")

# os.rename("oldname.txt","newname.txt")


# => Delete a file
# os.remove("newname.txt")

# => check file or dir exists or not
url = "l54sysmodule.py"
url = "abc"

if(os.path.exists(url)):
     print(f"{url} exists")
else:
     print(f"{url} does not exists.")


# Check file or dir
# url = "l54sysmodule.py"
url = "abc"

print("Is file: ",os.path.isfile(url))
print("Is directory: ",os.path.isdir(url))



# Check file or dir size
# url = "l54sysmodule.py"
url = "abc"

print("Size: ",os.path.getsize(url)," bytes") # Size:  1193  bytes

# Get file or dir created,modified, accessed
# url = "l54sysmodule.py"
url = "abc"

print("Created: ",time.ctime(os.path.getctime(url))) # Created:  Sun Aug 10 15:09:19 2025
print("Modified: ",time.ctime(os.path.getmtime(url))) # Modified:  Sun Aug 10 15:40:34 2025
print("Accessed: ",time.ctime(os.path.getatime(url))) # Accessed:  Sun Aug 10 20:28:18 2025


# => Set and Get environment variable
os.environ["GREETING"] = "Hello Mandalay"
print(os.environ.get("GREETING")) # Hello Mandalay


# => Path join 
filepath = os.path.join("folder","subfolder","app.py")
print(filepath) # folder\subfolder\app.py

# => absolute Path
print(os.path.abspath("package.json")) # D:\datalandcourses\pythonbatch1\part3\package.json

# => Split file name extension
filename = "cutedog.jpg"
print(os.path.splitext(filename)) # ('cutedog', '.jpg')

