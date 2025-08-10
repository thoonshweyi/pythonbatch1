import sys

# print("Enter your name : ")
# userinput = sys.stdin.readline()
# print(f"Your name is : {userinput}")

sys.stderr.write("This is an error message \n")
sys.stdout.write("This is standard output \n")

print(sys.version) # 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)]
print(sys.platform) # win32 
print(sys.path) # 
print(sys.argv) #['l54sysmodule.py'] # ['l54sysmodule.py', 'hello']

print(sys.argv[0]) # l54sysmodule.py
print(sys.argv[1]) # python3 l54sysmodule.py hello
print(sys.argv[2]) # python3 l54sysmodule.py hello sir
print(sys.argv[1:]) #python3 l54sysmodule.py hello sir # ['hello', 'sir']



print("Before exit")
sys.exit()
print("After exit")


# *result (sys.path)
# ['D:\\datalandcourses\\pythonbatch1\\part3', 
#  'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip', 
#  'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\DLLs', 
#  'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\Lib', 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312', 
#  'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages'
#  ]
