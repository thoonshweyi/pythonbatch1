import re

pattern = re.compile(r"\d")

text = "I want to the store and bought 5 apples, 4 orange, and 20 mangos"
print(pattern.findall(text)) # ['5', '4', '2', '0']

pattern = re.compile(r"\D")
print(pattern.findall(text)) #['I', ' ', 'w', 'a', 'n', 't', ' ', 't', 'o', ' ', 't', 'h', 'e', ' ', 's', 't', 'o', 'r', 'e', ' ', 'a', 'n', 'd', ' ', 'b', 'o', 'u', 'g', 'h', 't', ' ', ' ', 'a', 'p', 'p', 'l', 'e', 's', ',', ' ', ' ', 'o', 'r', 'a', 'n', 'g', 'e', ',', ' ', 'a', 'n', 'd', ' ', ' ', 'm', 'a', 'n', 'g', 'o', 's']
# Not Digit

pattern = re.compile(r"\w")
print(pattern.findall(text)) # ['I', 'w', 'a', 'n', 't', 't', 'o', 't', 'h', 'e', 's', 't', 'o', 'r', 'e', 'a', 'n', 'd', 'b', 'o', 'u', 'g', 'h', 't', '5', 'a', 'p', 'p', 'l', 'e', 's', '4', 'o', 'r', 'a', 'n', 'g', 'e', 'a', 'n', 'd', '2', '0', 'm', 'a', 'n', 'g', 'o', 's']
# Only Word

pattern = re.compile(r"\W")
print(pattern.findall(text)) #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ',', ' ', ' ', ',', ' ', ' ', ' ']
# Only Special characters

pattern = re.compile(r"\s")
print(pattern.findall(text)) # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# space

pattern = re.compile(r"\S")
print(pattern.findall(text)) # ['I', 'w', 'a', 'n', 't', 't', 'o', 't', 'h', 'e', 's', 't', 'o', 'r', 'e', 'a', 'n', 'd', 'b', 'o', 'u', 'g', 'h', 't', '5', 'a', 'p', 'p', 'l', 'e', 's', ',', '4', 'o', 'r', 'a', 'n', 'g', 'e', ',', 'a', 'n', 'd', '2', '0', 'm', 'a', 'n', 'g', 'o', 's']
# word + special char

# ----------------------------------------

greeting = "Hello."

pattern = re.compile(r"e..o")
print(pattern.findall(greeting)) # ['ello']

pattern = re.compile(r"\.")
print(pattern.findall(greeting)) # ['.']

# ---------------------------------------

sayhi = "Hi Aung Aung"

pattern = re.compile(r"[iAg]")
print(pattern.findall(sayhi)) # ['i', 'A', 'g', 'A', 'g']

pattern = re.compile(r"[^giA]")
print(pattern.findall(sayhi)) # ['H', ' ', 'u', 'n', ' ', 'u', 'n']

# -------------------------------------------------
string = "bbb bbb bbbb bbbbb"

pattern = re.compile(r"b{3}")
print(pattern.findall(string)) # ['bbb', 'bbb', 'bbb', 'bbb']

pattern = re.compile(r"b{3,}")
print(pattern.findall(string)) # ['bbb', 'bbb', 'bbbb', 'bbbbb']

pattern = re.compile(r"b{4}")
print(pattern.findall(string)) # ['bbbb', 'bbbb']

pattern = re.compile(r"b{4,}")
print(pattern.findall(string)) # ['bbbb', 'bbbbb']

pattern = re.compile(r"b{4,4}")
print(pattern.findall(string)) # ['bbbb', 'bbbb']

pattern = re.compile(r"b{4,5}")
print(pattern.findall(string)) # ['bbbb', 'bbbbb']
# --------------------------------------
sayhello = "hello   goodbye"

pattern = re.compile(r"\s{1}")
print(pattern.findall(sayhello)) # [' ', ' ', ' ']

pattern = re.compile(r"\s{2}")
print(pattern.findall(sayhello)) # ['  ']


pattern = re.compile(r"\s{3}")
print(pattern.findall(sayhello)) # ['   ']

pattern = re.compile(r"\s{3,}")
print(pattern.findall(sayhello)) # ['   ']

pattern = re.compile(r"\s{4}")
print(pattern.findall(sayhello)) # []
# --------------------------------
mynums = "123 4567 789 10"
pattern = re.compile(r"\d{3}")
print(pattern.findall(mynums)) # ['123', '456', '789']


pattern = re.compile(r"\d{4}")
print(pattern.findall(mynums)) # ['4567']
# --------------------------------

# => Bountary 
# note: \bt = start 
#         t\b = end
#         \Bt = not start (middle or end)
#         t\B = not end (middle or end)

mystring = "this test to try"

pattern = re.compile(r"\bt")
print(pattern.findall(mystring)) # ['t', 't', 't', 't']


pattern = re.compile(r"t\b")
print(pattern.findall(mystring)) # ['t']

pattern = re.compile(r"t\B")
print(pattern.findall(mystring)) # ['t', 't', 't', 't']

# --------------------------------
# ^ shift+ 6

mycards = "My credit card number is 555-123-4567 nd my debit card number is 555-123-5566. Thank you."

pattern = re.compile(r"\d{3}")
print(pattern.findall(mycards)) # ['555', '123', '456', '555', '123', '556']

pattern = re.compile(r"\d{3}-\d{3}")
print(pattern.findall(mycards)) # ['555-123', '555-123']

pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
print(pattern.findall(mycards)) # ['555-123-4567', '555-123-5566']


mycards = "My credit card number is 555   123   4567 nd my debit card number is 555   123    5566. Thank you."

pattern = re.compile(r"\d{3}\s{1,}\d{3}\s{1,}\d{4}")
print(pattern.findall(mycards)) # ['555   123   4567', '555   123    5566']

pattern = re.compile(r"\d{3}\s+\d{3}\s+\d{4}") # one or more
print(pattern.findall(mycards)) # ['555   123   4567', '555   123    5566']

pattern = re.compile(r"\d+\s+\d+\s+\d+") # one or more
print(pattern.findall(mycards)) # ['555   123   4567', '555   123    5566']
# -------------------------------------------------