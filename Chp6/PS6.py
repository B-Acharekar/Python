# 1. Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))
c = int(input("Enter number 3 :"))
d = int(input("Enter number 4 :"))

if ( a>b and a>c and a>d):
    print("Greatest number is a: ", a)
elif(b>a and b>c and b>d):
    print("Greater number is b: ", b)
elif(c>a and c>b and c>d):
    print("Greater number is c: ", c)
elif(d>a and d>b and d>b):
    print("Greater number is d: ", d)

# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user
marks1 = int(input("Enter marks 1 :"))
marks2 = int(input("Enter marks 2 :"))
marks3 = int(input("Enter marks 3 :"))

# Check for total percentage
total_percentage = ((marks1 + marks2 + marks3)/300) *100

if (total_percentage >= 40) :
    # Check for at least 33% in each subject
    if (marks1 >= 33 and marks2 >= 33 and marks3 >= 33) :
        print("Student has passed:",total_percentage)
    else :
        print("Student has failed in at least one subject:",total_percentage)

else :
    print("Student has failed, try again next year:",total_percentage)

# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

p1= "Make a lot of money"
p2= "buy now"
p3= "subscribe this"
p4= "click this"

message =  input("Enter your comment: ")

if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("Spam detected in comment")
else:
    print("No spam detected in comment")

# 4. Write a program to find whether a given username contains less than 10
# characters or not.

username = input("Enter your username: ")

if (len(username)<10):
    print("Username contains less than 10 characters")
else:
    print("Valid username")

# 5. Write a program which finds out whether a given name is present in a list or not.
a = ["Harry","John","Anushka","Riya","Vedant","Shubham"]

name = input("Enter a name to check: ")
if ( name in a ):
    print("Name found in the list")
else:
    print("Name not found in the list")

# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter your marks:"))

if ( marks<=100 and marks>=90):
    print("Grade: Ex")
elif ( marks<=89 and marks>=80):
    print("Grade: A")
elif ( marks<=79 and marks>=70):
    print("Grade: B")
elif ( marks<=69 and marks>=60):
    print("Grade: C")
elif ( marks<=59 and marks>=50):
    print("Grade: D")
elif( marks<=49):
    print("Grade: F")

# 7. Write a program to find out whether a given post is talking about “Harry” or not.
word = "Harry"

post = input("Enter the post: ")

if (word.lower() in post.lower()):
    print("Post is talking about Harry")
else:
    print("Post is not talking about Harry")