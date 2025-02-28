# => all (iterable)

# Note (truthy): Non-zero numbers, non-empty, True
# Note (falsy): 0, none, False

# => any (iterable)

# Note (truthy): at least one element it truthy

# boollists = [True,True,True]
# print(all(boollists)) #True
# print(any(boollists)) #True

# boollists = [True,False,True] 
# print(all(boollists))#False
# print(any(boollists))#True

# numlists = [1,2,3,4,5]
# print(all(numlists))  #True
# print(any(numlists))  #True


# numlists = [1,2,0,4,5]
# print(all(numlists)) #False
# print(any(numlists)) #True

# emptylist = []
# print(all(emptylist))  #True
# print(any(emptylist))  #False

# # =>Tuple 
# booltuple = (True,True,True)
# print(all(booltuple))  #True
# print(all(booltuple))  #True

# # # =>Set 
# numset = {1,2,3,4,0}
# print(all(numset))  #False
# print(any(numset))  #True

# # =>Dictionary
# colordict = {1:"red",2:"green",3:"blue"}
# print(all(colordict))  #True
# print(any(colordict))  #True

# colordict = {1:"red",0:"green",3:"blue"}
# print(all(colordict))  #False
# print(any(colordict))  #True

# # using Cases 
# stringlists = ["red","green","blue"]
# print(all(stringlists)) #True
# print(any(stringlists)) #True

# stringlists = ["red","","blue"]
# print(all(stringlists)) #False
# print(any(stringlists)) #True


# # Check all numbers are positive
# numlists = [10,20,30,40,50]
# checkpositive = all(num > 0 for num in numlists)
# print(checkpositive)

# numlists = [10,-20,30,40,50]
# checkpositive = all(num > 0 for num in numlists)
# print(checkpositive)

# =>Validate a list of condition 
requiredfields = ["username","email","password"]

users = {
     "username":"su su",
     "email":"susu@gmail.com",
     "password":"123456789",
}

# print("username" in users)
# print(field in users and users[field] for field in requiredfields)

getresult = all(field in users and users[field] for field in requiredfields) # all([True,True,True])
print(getresult)

# Explaination
# "username" in users = True
# users['username'] = su su (truthy) = True

# 2AA