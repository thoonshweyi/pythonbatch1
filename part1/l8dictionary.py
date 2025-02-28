# Method 1
student = {
     "name" : "Su Su",
     "age": 20,
     "city": "Yangon"
}

print(student) #{'name': 'Su Su', 'age': 20, 'city': 'Yangon'}
print(student['name']) # Su Su
print(student.get('city')) # Yangon

# Method 2 dict()
staff = dict(name="Aung Aung",age=30,city="Mandalay")
print(staff) # {'name': 'Aung Aung', 'age': 30, 'city': 'Mandalay'}
print(staff["age"]) # 30
print(staff.get("city")) # Mandalay


# print(student["country"]) # KeyError: 'country'
# print(staff['country']) # KeyError: 'country'

print(student.get("country")) # None
print(staff.get('country')) # None

# Default value for not existing property
print(student.get('country',"Myanmar"))
print(staff.get('country',"Thailand"))
# Default value for existing property
print(student.get('age',40))
print(staff.get('age',50))


employee = {
     "name": "Aung Aung",
     "age": 30,
     "city": "Mandalay"
}
print(employee) # {'name': 'Aung Aung', 'age': 30, 'city': 'Mandalay'}

employee["email"] = "aungaung@gmail.com"
print(employee) # {'name': 'Aung Aung', 'age': 30, 'city': 'Mandalay', 'email': 'aungaung@gmail.com'}


employee["age"] = 25
print(employee) # {'name': 'Aung Aung', 'age': 25, 'city': 'Mandalay', 'email': 'aungaung@gmail.com'}

del employee['city']
print(employee) # {'name': 'Aung Aung', 'age': 25, 'email': 'aungaung@gmail.com'}



worker = dict(name="Nilar",age=18,city="Bago")
print(worker) # {'name': 'Nilar', 'age': 18, 'city': 'Bago'}
worker["email"] = "nilar@gmail.com"
print(worker) # {'name': 'Nilar', 'age': 18, 'city': 'Bago', 'email': 'nilar@gmail.com'}


worker["age"] = 25
print(worker) # {'name': 'Nilar', 'age': 25, 'city': 'Bago', 'email': 'nilar@gmail.com'}

del worker['city']
print(worker) # {'name': 'Nilar', 'age': 25, 'email': 'nilar@gmail.com'}

