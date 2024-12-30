# Functions in Python are blocks of reusable code that perform specific tasks.
# They help reduce repetition, organize code, and make it more readable and manageable.

# Example WITHOUT Functions
# Here, the same code is repeated twice to calculate the average of three numbers.

# First set of inputs and calculations
a = int(input("Enter a number: "))  # Input the first number
b = int(input("Enter a number: "))  # Input the second number
c = int(input("Enter a number: "))  # Input the third number

# Calculate the average of the three numbers
average = (a + b + c) / 3
print("Average:", average)  # Print the result

# Same code repeated again for another set of numbers
a = int(input("Enter a number: "))  # Input the first number
b = int(input("Enter a number: "))  # Input the second number
c = int(input("Enter a number: "))  # Input the third number

# Calculate the average again
average = (a + b + c) / 3
print("Average:", average)  # Print the result

# The above code is repetitive. Let's improve it using a FUNCTION!

# Example WITH Functions
# Define a function to calculate and print the average
def avg():
    # Input three numbers
    a = int(input("Enter a number: "))  # First number
    b = int(input("Enter a number: "))  # Second number
    c = int(input("Enter a number: "))  # Third number

    # Calculate the average
    average = (a + b + c) / 3
    print("Average:", average)  # Print the average

# Function call
# Instead of repeating the same code, we just call the function whenever needed.
avg()  # First call to calculate average
avg()  # Second call to calculate average

# There are two types of functions in python:
# 1. Built in functions (Already present in python)
# 2. User defined functions (Defined by the user)
# Examples of built in functions includes len(), print(), range() etc