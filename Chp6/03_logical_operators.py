# Logical Operators Example

a = int(input("Enter your age: "))

# 'and' checks if both conditions are True
if a > 0 and a < 18:  # Age is valid and less than 18
    print("You are still a minor")
# End of if statement no. 1

# 'or' checks if at least one condition is True
if a < 0 or a > 150:  # Age is either invalid or unrealistically high
    print("You might have entered an invalid age")
# End of if statement no. 2

# 'not' inverts the result of the condition
if not (a >= 18):  # If the age is not 18 or more
    print("You are not an adult yet")
else:
    print("Your adult")
# End of if statement no. 3