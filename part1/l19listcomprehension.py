# =>List Comprehension

# {expression for item in iterable condition}
                    # 0 to 4
squares = [ x**2 for x  in range(5)]
print(squares) # {0, 1, 4, 9, 16}

# 0 ** 2 = 0
# 1 ** 2 = 1
# 2 ** 2 = 4
# 3 ** 2 = 9
# 4 ** 2 = 16

evens = [ x for x in range(10) if x%2 == 0]
print(evens) # [0, 2, 4, 6, 8]

chars = [ char for char in "hello world" ]
print(chars) # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']


numbers = [1,2,2,3,4,7,5,7]
uniqnumbers = [x for x in numbers]
print(uniqnumbers) # [1, 2, 2, 3, 4, 7, 5, 7]

# => Nested Loops in set comprehension 
couplenums = [ (x,y) for x in range(3) for y in range(2)]
print(couplenums) # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

# => Nested list comprehension

nestednumberarr = [[1,2,3],[40,50,60],[700,800,900]]
flatarrs = [y for x in nestednumberarr for y in x]
print(flatarrs) # [1, 2, 3, 40, 50, 60, 700, 800, 900]

# for x in nestednumberarr
# first iteration x = [1,2,3]
# second iteration x = [40,50,60]
# third iteration x = [700,800,900]

# for y in x
# first iteration x = [1,2,3], processes y = 1, y = 2, y = 3
# second iteration x = [40,50,60]  processes y = 40, y = 50, y = 60
# third iteration x = [700,800,900] processes y = 700, y = 800, y = 900