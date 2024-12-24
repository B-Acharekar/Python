name = "harry"

# len() function – This function returns the length of the string.
print(len(name))  # Output: 5

# String.endswith("rry") – This function tells whether the variable string ends with
# the string "rry" or not.
print(name.endswith("rry"))  # Output: True

# String.startswith("ha") – This function tells whether the variable string starts with
# the string "ha" or not.
print(name.startswith("ha"))  # Output: True

# String.count("r") – This function returns the count of the given substring in the string.
print(name.count("r"))  # Output: 2

# String.capitalize() – This function capitalizes the first character of the string.
print(name.capitalize())  # Output: Harry

# String.find("rr") – This function returns the first index of the given substring in the string. 
# If not found, it returns -1.
print(name.find("rr"))  # Output: 2

# String.lower() – This function converts all the characters in the string to lowercase.
print(name.lower())  # Output: harry

# String.upper() – This function converts all the characters in the string to uppercase.
print(name.upper())  # Output: HARRY

# String.replace("r", "z") – This function replaces all occurrences of "r" with "z".
print(name.replace("r", "z"))  # Output: hazzy

# String.strip() – This function removes any leading and trailing spaces from the string.
name_with_spaces = "   harry   "
print(name_with_spaces.strip())  # Output: "harry"

# String.split("r") – This function splits the string at each occurrence of "r".
print(name.split("r"))  # Output: ['ha', '', 'y']

# String.isalpha() – This function checks whether the string contains only alphabetic characters.
print(name.isalpha())  # Output: True

# String.isdigit() – This function checks whether the string contains only digits.
num_string = "12345"
print(num_string.isdigit())  # Output: True

# String.isalnum() – This function checks whether the string contains only alphanumeric characters.
alnum_string = "Harry123"
print(alnum_string.isalnum())  # Output: True

# String.swapcase() – This function swaps uppercase letters to lowercase and vice versa.
mixed_case = "HaRrY"
print(mixed_case.swapcase())  # Output: hArRy

# String.title() – This function converts the first character of each word to uppercase.
sentence = "hello world"
print(sentence.title())  # Output: Hello World

