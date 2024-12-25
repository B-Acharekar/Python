# 1. Write a program to store seven fruits in a list entered by the user.
fruits = []
f1 = input("Enter fruits name: ")
fruits.append(f1)
f2 = input("Enter fruits name: ")
fruits.append(f2)
f3 = input("Enter fruits name: ")
fruits.append(f3)
f4 = input("Enter fruits name: ")
fruits.append(f4)
f5 = input("Enter fruits name: ")
fruits.append(f5)
f6 = input("Enter fruits name: ")
fruits.append(f6)
f7 = input("Enter fruits name: ")
fruits.append(f7)

print(fruits)

# 2. Write a program to accept fruits of 6 students and display them in a sorted manner.
marks = []
f1 = int(input("Enter marks here: "))
marks.append(f1)
f2 = int(input("Enter marks here: "))
marks.append(f2)
f3 = int(input("Enter marks here: "))
marks.append(f3)
f4 = int(input("Enter marks here: "))
marks.append(f4)
f5 = int(input("Enter marks here: "))
marks.append(f5)
f6 = int(input("Enter marks here: "))
marks.append(f6)
marks.sort()
print(marks)

# 3. Check that a tuple type cannot be changed in python.
a = (34,234,"Tony")
a[2] = "John" #Will give error 

# 4. Write a program to sum a list with 4 numbers.

l1 = [34,55,72,8]
print(sum(l1)) # Sum(): is the function which sum up all numbers and returns the value

# 5. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
count = a.count(0)
print(count)