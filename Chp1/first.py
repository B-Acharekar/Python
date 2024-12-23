print("Hello world")

# This is a comment
"""this a 
multi-line comment"""

# problem1
# Write a program to print Twinkle twinkle little star poem in python
print('''
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.''')

# problem2
# 2. Use REPL and print the table of 5 using it. 
for i in range(1, 11):
    print("5 x", i, "=", 5*i)

# problem3
# Install an external module and use it to perform an operation of your interest. 

    # To install a module:
    # pip install <module_name>

    # For example, to install the flask module:
    # pip install flask

# problem4
# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 

import os

# Specify the directory to list (use '.' for the current directory)
directory = '/bhush'

try:
    contents = os.listdir(directory)
    print(f"Contents of the directory '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory}'.")


