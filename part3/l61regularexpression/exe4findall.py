import re

# exe 1 (contains abc) - whatever it position
text = "123abc456"
pattern = r"abc"

match = re.search(pattern,text)
print("Match found" if match else "No match")

# exe 2 (match only at the beginning of a string)
text = "456abc"
pattern = r"abc"

if re.match(pattern,text):
     print("Pattern found at the begiing.")


# exe 3 (find all digits)
text = "Product123 costs $456 and qty is 789"
pattern = r"\d+"

result = re.findall(pattern,text)
print("Found digits: ",result) # Found digits:  ['123', '456', '789']

# exe 4 (split = string numeric)

text = "apple,banana,orange|mango 12345"
pattern = r"\W+"

result = re.split(pattern,text)
print("Split parts W: ",result) # Split parts:  ['apple', 'banana', 'orange', 'mango', '12345']

# exe 4 (split = )

text = "apple,banana; orange|mango 12345"
pattern = r"\w+"

result = re.split(pattern,text)
print("Split parts w: ",result) # Split parts w:  ['', ',', '; ', '|', ' ', '']
# Seperate by non word character, think of word characters as delimiter
# "apple,banana; orange|mango 12345"
# "$,$; $|$ $"

# exe 5 (replace all = )

text = "Python is fun and powerful"
pattern = r"\s"

result = re.sub(pattern,"-",text)
print("Replaced: ",result) # Replaced:  Python-is-fun-and-powerful



# => Validate phone number format
phones = ["098-765-4321","0987654321","555-abc-1234","098-7654-321"]
pattern = r"^\d{3}-\d{3}-\d{4}$"

for phone in phones:
     if re.match(pattern,phone):
          print(f"{phone} is valid.")
     else:
          print(f"{phone} is invalid")

# => Validate password format

pattern = re.compile(r"[A-Za-z0-9@#$]{8,}")
password = "abc123"

check = pattern.fullmatch(password)
print("Valid Password Format" if check else "Invalid")

# => Extract email addresses, fullmatch()
text = "Contact us at support@gmail.com or admin@shop.org.Thank you."
pattern = r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+"

emails = re.findall(pattern,text)
print("Emails: ",emails) # Emails:  ['support@gmail.com', 'admin@shop.org']

# -------------------------------------------------------------------------------------------
# re.match()

# re.match(pattern, string)
# Tries to match the pattern only at the beginning of the string.

# If the pattern is found at the start → returns a match object.

# If not → returns None.


# 🔹 re.fullmatch()

# Tries to match the entire string against the regex pattern.

# If the whole string matches → returns a Match object.

# If only part of it matches, or nothing matches → returns None.