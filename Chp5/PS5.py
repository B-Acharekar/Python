# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

words = {
    "madad": "Help",
    "billi": "Cat",
    "kusri": "Chair"
}

word = input("Enter the words you want meaning of: ")
print(words[word])

# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once)

s = set()
n = int(input("Enter the number 1: "))
s.add(n)
n = int(input("Enter the number 2: "))
s.add(n)
n = int(input("Enter the number 3: "))
s.add(n)
n = int(input("Enter the number 4: "))
s.add(n)
n = int(input("Enter the number 5: "))
s.add(n)
n = int(input("Enter the number 6: "))
s.add(n)
n = int(input("Enter the number 7: "))
s.add(n)
n = int(input("Enter the number 8: "))
s.add(n)
print("set: ", s)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s = set()
s.add(18)
s.add("18")
print(s) #Yes, we can have 18 as int & str in set

# 4. What will be the length of following set s:

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print("length:", len(s))

# 5. s = {}
# What is the type of 's'?
s = {}
print(type(s)) # It is a dictionary

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
d = {}

name = input("Enter friends name:")
lang = input("Enter Language name: ")
d. update({name: lang})

name = input("Enter friends name:")
lang = input("Enter Language name: ")
d. update({name: lang})

name = input("Enter friends name:")
lang = input("Enter Language name: ")
d. update({name: lang})

name = input("Enter friends name:")
lang = input("Enter Language name: ")
d. update({name: lang})

print(d)

# 7. If the names of two friends are the same, what will happen in the program in problem 6?
# If keys are the same, the value will be updated. 
# For example, {"rohan": "c"} will be updated to {"rohan": "Js"}.

# 8. If the languages of two friends are the same, what will happen in the program in problem 6?
# In a dictionary, values can be identical for different keys, but each key must be unique.

# 9. Can you change the values inside a list that is contained in set S?

s = {8, 7, 12, "Harry", [1, 2]}  # This will raise a TypeError because sets cannot contain mutable elements like lists.

# Explanation:
# Sets only allow immutable (unchangeable) elements. Since lists are mutable, they cannot be added to a set.

# Example:
# s[3] = 10  # This will not work, as sets do not support indexing or mutable elements.
