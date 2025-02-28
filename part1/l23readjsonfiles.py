import json
import os
# =>Reading JSON from a string (loads)
jsonstring = '{"name":"Hsu Myat Noe","age":18,"isstudent":true}'
datas = json.loads(jsonstring)
print(datas)
print(datas["name"])
print(datas["age"])

# => Reading a simple JSON file (load for json format)
def readjson(filename):
     with open(filename,'r') as file:
          datas = json.load(file)
     return datas

getsimplejson = readjson('files/file8.json')
print(getsimplejson)
print(getsimplejson["name"])
print(getsimplejson["age"])
print(getsimplejson["hobbies"][0])
print(getsimplejson["hobbies"][1])


# => Reading a simple JSON Array file (load for json format)
getarrayjsons = readjson("files/file9.json")
print(getarrayjsons)
for getarrayjson in getarrayjsons:
     print(f"Name: {getarrayjson["name"]}, Age: {getarrayjson['age']}")

# => Reading a complex JSON  file (load for json format)
getcomplexjsons = readjson("./files/file10.json")
print(getcomplexjsons)
print(getcomplexjsons["company"])
getproduct = getcomplexjsons["product"]
print(getproduct[0]["name"])
print(getproduct[1]["price"])

# => Error Handling (check file exist or not)
try:
     with open("files/file10.json","r") as file:
          datas = json.load(file)
except FileNotFoundError as e:
     print("Error: File not found.",str(e))
except json.JSONDecodeError as e:
     print("Error: Invalid JSON format!",str(e))
else:
     print(datas)

getfile = "files/file10.json"

if not os.path.isfile(getfile):
     print(f"Error: File{getfile} does not exist.")
else:
     with open(getfile,'r') as file:
          data = json.load(file)
          print(datas)


# What is json.loads()?
# json.loads() stands for "load string".
# It parses a JSON string and returns a corresponding Python object (usually a dictionary).

# What Does os.path.isfile() Do?
# os.path.isfile(getfile) → Checks if getfile is a file that exists.
# Returns True → If the file exists.
# Returns False → If the file does not exist
#  Explanation of os.path Module
# The os module in Python provides functions to interact with the operating system.
# The os.path submodule contains file and directory-related functions.