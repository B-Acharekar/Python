marks = {
    "Aryan": 56,       # Key: 'Aryan', Value: 56
    "John": 79,
    "Ved": 52,
    "list": [1, 2, 3]  # Values can be of any data type
}

# Dictionary methods for easy data handling

# 1. .items() - Get all key-value pairs as tuples
print(marks.items())  # Output: dict_items([('Aryan', 56), ('John', 79), ...])

# 2. .keys() - Get all keys
print(marks.keys())  # Output: dict_keys(['Aryan', 'John', 'Ved', 'list'])

# 3. .values() - Get all values
print(marks.values())  # Output: dict_values([56, 79, 52, [1, 2, 3]])

# 4. .update() - Update or add key-value pairs
marks.update({"John": 99, "Renuka": 82})  # Updates 'John' and adds 'Renuka'
print(marks)

# 5. .get() - Returns the value of the specified key
print(marks.get("Areen"))  # Output: None (no error if key doesn't exist)
print(marks.get("John"))   # Output: 99
print(marks["John"])       # Output: 99 (KeyError if key doesn't exist)

# 6. .pop() - Removes a specified key and returns its value
removed_value = marks.pop("Ved")
print(removed_value)  # Output: 52
print(marks)          # Key 'Ved' is now removed from the dictionary

# 7. .popitem() - Removes the last inserted key-value pair (from Python 3.7+)
last_item = marks.popitem()
print(last_item)  # Output: ('Renuka', 82) (last key-value pair removed)
print(marks)

# 8. .clear() - Removes all elements from the dictionary
marks.clear()
print(marks)  # Output: {}

# 9. Copy a dictionary using .copy()
marks = {"Aryan": 56, "John": 79}
marks_copy = marks.copy()
print(marks_copy)  # Output: {'Aryan': 56, 'John': 79}

# 10. Set default value using .setdefault()
default_value = marks.setdefault("Ved", 45)  # Adds 'Ved' if not already present
print(marks)  # Output: {'Aryan': 56, 'John': 79, 'Ved': 45}
print(default_value)  # Output: 45

# 11. Create a dictionary from keys using .fromkeys()
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)  # Creates {'a': 0, 'b': 0, 'c': 0}
print(default_dict)
