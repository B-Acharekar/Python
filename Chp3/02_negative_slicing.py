name = "harry"

# String slicing for substrings:
# The syntax is name[start:stop:step]
# start: The starting index (inclusive). Defaults to 0 if omitted.
# stop: The ending index (exclusive). Defaults to the string length if omitted.
# step: The step or increment. Defaults to 1 if omitted.

# Examples:
first_three = name[0:3]  # Characters from index 0 up to (but not including) 3.
print(first_three)

last_two = name[3:]  # Characters from index 3 to the end of the string.
print(last_two)

every_other = name[::2]  # Every other character, starting from the beginning.
print(every_other)

reversed_name = name[::-1] # Reverses the string
print(reversed_name)

# Negative indexing: Accessing characters from the end of the string.
last_char = name[-1]  # The last character.
print(last_char)

second_to_last = name[-2] # The second to last character
print(second_to_last)
