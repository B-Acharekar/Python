# Intro to strings
# String : It is a sequence of characters enclosed in quotes.It is a datatype in Python
# We can primarily write a string in these three ways
a =  "Bhushan" # Single quote string
b = 'Bhushan'  # Dobule quote string
c = '''hello,
this is a muitline statement''' # Triple quote string: Used for multi-line statements
print(c)

# String Slicing: Extracting parts of a string in Python.

name = "harry"  # String length: 5. Strings are zero-indexed (start at 0).
# to find the length of a string we use :
print(f"length of string '{name}' is: {len(name)}")
# Accessing individual characters:
first_char = name[0]  # Accesses the character at index 0 (the first character).
print(f"The first character of '{name}' is: {first_char}")

# In order to slice a string, we use the following syntax:
nameShort = name[0:3] #Start from index 0 all the way till 3 (excluding 3)
print(nameShort)

