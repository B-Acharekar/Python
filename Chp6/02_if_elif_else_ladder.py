# IF-ELIF-ELSE Ladder

# Taking user input for age
a = int(input("Enter your age: "))

# Demonstrating multiple conditions in sequence
if (a < 10):  # If age is less than 10
    print("You are a child")
elif (a >= 10 and a < 18):  # If age is between 10 (inclusive) and 18 (exclusive)
    print("You are a teenager")
elif (a >= 18 and a < 60):  # If age is between 18 (inclusive) and 60 (exclusive)
    print("You are an adult")
else:  # If none of the above conditions are True
    print("You are a senior citizen")