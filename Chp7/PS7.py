# 1. Write a program to print multiplication table of a given number using for loop.
# n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{n} x {i} = { n * i}")

# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if name.startswith("S"):
#         print(f"Hello, {name}!")

# 3. Attempt problem 1 using while loop.

# n = int(input("Enter a number: "))

# i = 1
# while (i < 11):
#     print(f"{n} x {i} = { n * i}")
#     i += 1

# 4. Write a program to find whether a given number is prime or not

# num = int(input("Enter a number: "))

# for i in range(2,num):
#     if(num %i == 0):
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")

# 5. Write a program to find the sum of first n natural numbers using while loop

# n = int(input("Enter a number: "))

# i = 0 
# sum = 0

# while (i <= n):
#     sum += i
#     i += 1

# print(sum)

# 6. Write a program to calculate the factorial of a given number using for loop.

# n = int(input("Enter a number: "))

# fact = 1

# for i in range(1, n+1):
#     fact = fact * i

# print(fact)

# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

# n = int(input("Enter a number: "))  # Input the number of rows for the pattern

# # Loop through numbers from 1 to n (inclusive) to generate each row of the pattern
# for i in range(1, n+1):
#     # Print spaces to align the stars to the center
#     # " " * (n - i) creates the spaces needed before the stars
#     print(" " * (n - i), end="")  
    
#     # Print stars for the current row
#     # "*" * (2 * i - 1) calculates the number of stars in the current row
#     print("*" * (2 * i - 1), end="")
    
#     # Print a newline character to move to the next row
#     print("\n")

# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# n = int(input("Enter a number:"))

# for i in range (1,n+1):
#     print("*" * i)

# 9. Write a program to print the following star pattern.
# * * *
# * * for n = 3
# * * * 

# n = int(input("Enter a number:"))

# for i in range ( 1, n+1):
#     if (i==1 or i == n): 
#         print("*"*n,end="")
#     else: 
#         print("*",end="")
#         print(" "*(n-2),end ="")
#         print("*",end="")
#     print("")
     
# 10. Write a program to print multiplication table of n using for loops in reversed
# order.

n = int (input("Enter the number:"))

for i in range (1,11):
    print(f"{n} x {11-i} = {n * (11-i)}")