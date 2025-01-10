# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class Calculator:
    def __init__(self, num):
        self.num = num
    
    def square(self):
        print(f"The square of {self.num} is {self.num*self.num}")
    def cube(self):
        print(f"The cube of {self.num} is {self.num*self.num*self.num}")
    def sqrRoot(self):
        print(f"The square root of {self.num} is {self.num**1/2}")

n = int(input("Enter a number:"))
a = Calculator(n)
a.square()
a.cube()
a.sqrRoot()