# Recursion is a function that calls itself to solve smaller instances of a problem.
# It's like breaking a big task into smaller tasks until the solution is simple.

# Define a function to calculate factorial using recursion
def fact(n):
    # Base case: The simplest case that stops the recursion
    if n == 0 or n == 1:  # If n is 0 or 1, return 1 (factorial of 0 or 1 is 1)
        return 1 
    else:
        # Recursive case: The function calls itself with (n-1)
        return n * fact(n - 1)

# Example: Calculate factorial of 4
# Step-by-step breakdown:
# fact(4) = 4 * fact(3)
# fact(3) = 3 * fact(2)
# fact(2) = 2 * fact(1)
# fact(1) = 1 (base case)
# Now, it resolves like this: 4 * 3 * 2 * 1 = 24
a = fact(4)  # Call the function with n=4
print(a)  # Output: 24
