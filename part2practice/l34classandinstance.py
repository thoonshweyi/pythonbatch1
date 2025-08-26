class Car:
     SPEED_LIMIT:float = 150

     def __init__(self,brand:str)->None:
          self.brand = brand

     def drive(self,*,speed:float)->None:         # Keyword-Only Arguments. use by asterisk(*) key
          if speed > self.SPEED_LIMIT:
               print(f"Speed Limited activated: Drivig at {self.SPEED_LIMIT} km/h")
          else: 
               print(f"Driving at {speed} km/h")


def main()->None:
     bmw:Car = Car("BMW")
     bmw.drive(speed=100)
     # bmw.drive(160)

     bmw.SPEED_LIMIT = 170
     bmw.drive(speed=160)
     bmw.drive(speed=200)



if __name__ == "__main__":
     main()

# 2025-02-23

# 1. Positional Arguments

#           The most common type.

#           They are matched to function parameters by order.

#           Example:

#           def greet(name, age):
#           print(f"Hello {name}, you are {age} years old.")

#           greet("Alice", 25)   # ✅ position matters


#           Here:

#           "Alice" → name

#           25 → age

#           ⚠️ If you switch positions:

#           greet(25, "Alice")  # ❌ Wrong order, but still runs (not what we want)


#           Output:

#           Hello 25, you are Alice years old.

# 2. Keyword Arguments

#           You pass parameters by name, not just position.

#           Order doesn’t matter.

#           greet(age=25, name="Alice")   # ✅ works, order doesn’t matter


#           This makes your code clearer, especially with many parameters.

# 3. Mixing Positional and Keyword

#           You can use positional first, then keyword.

#           greet("Alice", age=25)   # ✅ valid


#           But you cannot do it the other way:

#           greet(name="Alice", 25)  # ❌ Error

# 4. Forcing Arguments

#           Python gives you tools to force how arguments must be passed.

#           (a) Normal (default behavior)
#           def add(a, b):
#           return a + b

#           add(3, 4)         # ✅ positional
#           add(a=3, b=4)     # ✅ keyword
#           add(3, b=4)       # ✅ mix

#           (b) Keyword-only arguments (*)
#           def drive(*, speed):
#           print(f"Driving at {speed} km/h")

#           drive(speed=100)   # ✅ must use keyword
#           drive(100)         # ❌ TypeError

#           (c) Positional-only arguments (/) (Python 3.8+)
#           def multiply(a, b, /):
#           return a * b

#           multiply(3, 4)      # ✅ positional only
#           multiply(a=3, b=4)  # ❌ TypeError: got some positional-only arguments

#           (d) Combined / and *

#           You can even combine both:

#           def func(a, b, /, c, d, *, e, f):
#           print(a, b, c, d, e, f)

#           # a, b → positional only
#           # c, d → can be either positional or keyword
#           # e, f → keyword only

#           func(1, 2, 3, d=4, e=5, f=6)  # ✅ correct
# 5. Why is this useful?

#      Clarity: forces caller to be explicit.

#      Safety: avoids accidental mistakes with parameter order.

#      Backward compatibility: library authors can add new parameters without breaking old code.

# ✅ Summary:

#      Positional arguments → order matters.

#      Keyword arguments → name matters, order doesn’t.

#      * → everything after must be keyword-only.

#      / → everything before must be positional-only.