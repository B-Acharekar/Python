# Dictionary is a collection of key-value pairs.

d = {} # empty dictionary
marks = {
    "Aryan": 56,  # 'Aryan' is the key, 56 is the value
    "John": 79,
    "Ved": 52,
    "list": [1, 2, 3]  # Values can also be lists, tuples, or other data types
}

# Accessing values using keys
print(marks["John"])  # Output: 79
print(marks["list"])  # Output: [1, 2, 3]

# PROPERTIES OF PYTHON DICTIONARIES:
# 1. It is unordered 
# 2. It is mutable 
# 3. It is indexed by keys, not numeric positions like lists.
# 4. Keys must be unique, but values can be duplicated.
