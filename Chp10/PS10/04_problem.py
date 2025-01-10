# 4. Add a static method in problem 2, to greet the user with hello.


class Calculator:
    def __init__(self, num):
        self.num = num
    
    def square(self):
        print(f"The square of {self.num} is {self.num*self.num}")
    def cube(self):
        print(f"The cube of {self.num} is {self.num*self.num*self.num}")
    def sqrRoot(self):
        print(f"The square root of {self.num} is {self.num**1/2}")

    @staticmethod  # Static method to greet the user
    def hello():
        print("Hello")

n = int(input("Enter a number:"))
a = Calculator(n)
a.hello()
a.square()
a.cube()
a.sqrRoot()