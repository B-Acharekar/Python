# 1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    elif (c > a and c > b):
        return c
    
a = 1
b = 2
c = 3
print(greatest(a,b,c))

# 2. Write a python program using function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(c):
    return (c * 9/5)+32

celsius = 25

print(celsius_to_fahrenheit(celsius))

# 3. How do you prevent a python print() function to print a new line at the end.

print("a",end="")
print("b")


# 4. Write a recursive function to calculate the sum of first n natural numbers

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

print(sum(5))

# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def pattern(n):
    if n == 0:
        return 
    print("*"*n)
    pattern(n-1)

pattern(3)

# 6. Write a python function which converts inches to cms.

def inches_to_cms(inch):
    return inch * 2.54

n = int(input("Enter a value in inches:"))
print(f"The above value in cm is {inches_to_cms(n)}")

# 7. Write a python function to remove a given word from a list ad strip it at the same
# time


def rem(l, word):
    n = []  # Initialize an empty list to store the result
    for item in l:
        if item != word:  # Check if the current item is not the word to remove
            n.append(item.strip())  # Strip extra spaces from the item and add it to the result
    return n  # Return the result list after processing all items

# Example list
l = ["harry", "bhushan", " aman ", "dave"]
print(rem(l, "harry"))  # Output: ['bhushan', 'aman', 'dave']

# 8. Write a python function to print multiplication table of a given number.
def multiplication_table(num):

    print(f"Multiplication Table for {num}:")
    for i in range(1, 11):  # Loop from 1 to 10
        print(f"{num} x {i} = {num * i}")  # Print the result in a formatted way

n = int(input("Enter a number to print its multiplication table: "))
multiplication_table(n)
