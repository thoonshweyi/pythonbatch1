lady = {"name":"Yadanar","age":30}
print(lady) #{'name': 'Yadanar', 'age': 30}
print(lady.get('name')) #Yadanar
print(lady.get('gender')) #None
print(lady.get('gender',"Not Defined")) #None

print(lady.keys()) # dict_keys(['name', 'age'])
print(list(lady.keys())) # ['name', 'age']
print(list(lady.keys())[0]) # name
print(list(lady.keys())[1]) # age

print(lady.values()) # dict_values(['Yadanar', 30])
print(list(lady.values())) # ['Yadanar', 30]
print(list(lady.values())[0]) # Yadanar
print(list(lady.values())[1]) # 30

print(lady.items()) # dict_items([('name', 'Yadanar'), ('age', 30)])
print(list(lady.items())) #[('name', 'Yadanar'), ('age', 30)]
print(list(lady.items())[0]) #('name', 'Yadanar')
print(list(lady.items())[1]) #('age', 30)
print(list(lady.items())[0][0]) #name
print(list(lady.items())[0][1]) #Yadanar
print(list(lady.items())[1][0]) #age
print(list(lady.items())[1][1]) #30

lady.update({'age':20,'gender':"female"})
print(lady) # {'name': 'Yadanar', 'age': 20, 'gender': 'female'}

lady.pop('age')
print(lady) # {'name': 'Yadanar', 'gender': 'female'}

lady.clear()
print(lady) # {}

# boy = {"name":"Zaw Zaw","city":"Yangon"}
# boy.pop()
# print(boy) #error


girl = {'name':"Yadanar","age":30,"city":"Mawlamyine"}
# girl.pop()
# print(girl) # TypeError: pop expected at least 1 argument, got 0

item = girl.popitem()
print(item) # ('city', 'Mawlamyine')
print(item[0]) # city
print(item[1]) # Mawlamyine

print(girl) # {'name': 'Yadanar', 'age': 30}

women = girl.copy() 
print(women) #{'name': 'Yadanar', 'age': 30}


# 3DM
# dictionary.get(key, default=None)
# The get() method in Python is used to retrieve the value associated with a specified key in a dictionary
# Parameters:
# key: The key whose value you want to retrieve.
# default (optional): The value to return if the key is not found. By default, this is None.


# The list() function in Python is used to create a list from an iterable object, 
# such as a string, tuple, dictionary, or any other object that supports iteration.
# Converts Iterables to Lists:
# If the input is already a list, it returns a copy.
# If the input is a string, it converts each character into a separate element.
# If the input is a dictionary, it returns a list of keys.

# The dict.keys() method returns a view object of the dictionary's keys. To work with the keys as a list, use list().


# The update() method in Python is used to add key-value pairs to a dictionary or update the values of existing keys. 
# It allows you to merge another dictionary or iterable of key-value pairs into the original dictionary.
# If the key exists in the dictionary, its value is updated.
# If the key does not exist, it is added to the dictionary.


# The popitem() method in Python is used to remove and return the last key-value pair from a dictionary. 
# This method modifies the dictionary in place by removing an element.
# Parameters:
# None. The popitem() method does not take any arguments.
# Returns:
# A tuple containing the key and value of the removed item.
# Raises:
# KeyError: If the dictionary is empty and popitem() is called.
# Summary Table
# Method	Removes	          Argument  Required	Return Value	     Raises KeyError if Empty
# pop()	A specific key	     Yes	     Value of the removed key	     ✅ Yes
# popitem()	Last key-value pair	No	     Tuple (key, value)	          ✅ Yes