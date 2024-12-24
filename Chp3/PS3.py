# 1.Write a python program to display a user entered name followed by Good Afternoon using input () function.

name = input("Enter your name: ")
print(f"Good Afternoon, {name}!")

# 2. Write a program to fill in a letter template given below with name and date.
letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''

filled_letter = letter.replace("<|Name|>", "Bhushan").replace("<|Date|>", "24 December")
print(filled_letter)

# 3. Write a program to detect double space in a string.
str = "This is  a string"
print(str.find("  "))

# 4. Replace the double space from problem 3 with single spaces.
replacedStr = str.replace("  "," ")
print(replacedStr)

# 5. Write a program to format the following letter using escape sequence characters.
ltr = "Dear Harry, \n\tThis python course is nice.\nThanks!"
print(ltr)