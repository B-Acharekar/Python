# conditions are expressions that evaluate to True or False

# Taking user input for age
a = int(input("Enter your age: "))

# IF Clause: Checking if the age is 18 or more
if (a >= 18):  # Relational operator (>=) checks if age is greater than or equal to 18
    print("You are above the age of consent")  # Executes if the condition is True
    print("Good for you!")

# ELIF Clause: Checking if the age is less than or equal to 0 (invalid input)
elif (a <= 0):  # Relational operator (<=) checks if age is less than or equal to 0
    print("Please enter a valid age")  # Executes if this condition is True and the previous condition is False

# ELSE Clause: If none of the above conditions are True, execute this block
else:
    print("You are below the age of consent")  # Executes when age is between 1 and 17


# End of program
print("End of program")

