# Tuples are similar to lists but are immutable 
# (cannot be changed after creation)

# Creating tuples
a = ()  # Empty tuple
a = (1,)  # Tuple with only one element requires a trailing comma
a = (1, 2, 3)  # Tuple with more than one element needs commas between items

# Tuple with mixed data types
fruits = ("apple", "orange", "banana", 7, False, "Akash")  

# Accessing elements using their index
print(fruits[1])  

# Checking the type of the tuple
print(type(fruits))  

# Tuples are immutable, so attempting to change an element will throw an error
# fruits[1] = "grapes"  # Uncommenting this will cause a TypeError

# Count occurrences of an element in the tuple
no = fruits.count(7)  
print(no)  

# Find the index of the first occurrence of an element
i = fruits.index(7)
print(i) 

# Tuple Operations:
# Concatenation: Combine two tuples using the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition: Repeat a tuple multiple times using the * operator.
repeated = (1, 2) * 3
print(repeated)  # Output: (1, 2, 1, 2, 1, 2)

# Slicing: Extract a portion of a tuple using square brackets.
sliced = fruits[1:4]
print(sliced)  # Output: ('orange', 'banana', 'apple')

# Membership Check: Use in and not in to check if an element exists in a tuple.
print("apple" in fruits)  # Output: True
print("grapes" not in fruits)  # Output: True

# Sorting: You can sort a tuple by converting it into a list.
numbers = (4, 1, 3, 2)
sorted_numbers = tuple(sorted(numbers))
print(sorted_numbers)  # Output: (1, 2, 3, 4)

# Tuple Unpacking: Assign elements of a tuple to variables.
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)  # Output: 10 20 30

# Max and Min: Find the maximum and minimum values in a tuple 
# (works for tuples with comparable data types).
numbers = (4, 1, 3, 2)
print(max(numbers))  # Output: 4
print(min(numbers))  # Output: 1
