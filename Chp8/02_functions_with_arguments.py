# A function can accept some value it can work with. We can put these values in the
# parentheses

# Write a program to greet a user with “Good day” using functions.
name = input("Enter your name: ")
def greet(n):
    print(f"Good day, {n.capitalize()} !!")

greet(name)

def goodday(name,ending):
    print(f"Good day, {name.capitalize()}!!")
    print(ending)
    return 'ok'

goodday("Aman","Arigato")
a = goodday("Aman","Arigato") #return value from goodday function will be store in a variable
print("a: "+ a)

#  default values 
def goodday(name,ending= "Thank you"):
    print(f"Good day, {name.capitalize()}!!")
    print(ending)
    return 'ok'

goodday("Aman") # default value will be used for ending if not provided in the function call