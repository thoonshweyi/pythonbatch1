# =>reduce

# syntax
# from functools import reduce
# reduce(function, iterable[,initialize])

from functools import reduce
messages = ["Hello","my","friend"]

result1 = reduce(lambda x,y: x+" "+y,messages)
print(result1)

numbers = [1,2,3,4,5]
result2 = reduce(lambda x,y: x * y,numbers)
print(result2) #15

result2 = reduce(lambda x,y: x + y,numbers)
print(result2) #120

# Explanation 
# 1 x 2 = 2
# 2 x 3 = 6
# 6 x 4 = 24
# 24 x 5 = 120


result3 = reduce(lambda x,y: x if x > y else y,numbers)
print(result3) # 5
# Explanation 
# 1 > 2 = 2
# 2 > 3 = 3
# 3 > 4 = 4
# 4 > 5 = 5


result4 = reduce(lambda x,y: x if x < y else y,numbers)
print(result4) # 1