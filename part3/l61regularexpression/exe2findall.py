import re

pattern = re.compile("flower")
text = "There are a lot of flowers in the flower fields. i love flower."

print(pattern.findall(text)) # ['flower', 'flower', 'flower']
print(pattern.findall("orange")) # []

for match in pattern.findall(text):
     print(match)

for match in pattern.finditer(text):
     print(match) # <re.Match object; span=(19, 25), match='flower'>



# => re.finditer()

# Definition:
# finditer() is a method in Python’s re (regular expression) module.
# It scans through a string, looking for all non-overlapping matches of a pattern.

# Return value:
# Instead of returning a list (like findall()), it returns an iterator that yields match objects one by one.



# What’s inside the match object?

# A re.Match object contains information about each match:

# .span() → the start and end indices of the match in the string.

# .start() / .end() → start and end positions separately.

# .group() → the actual substring that was matched.