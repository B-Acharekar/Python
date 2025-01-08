class Employee:
    # Class attributes
    name = "Yash"
    language = "Java"
    salary = "500000"

    # Instance method using the self parameter
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # Static method does not use the self parameter
    # Use @staticmethod to define a method that doesn't depend on instance or class variables
    @staticmethod
    def greet():
        print("Good morning!")

# Creating an instance (object) of the Employee class
obj = Employee()

# Calling the static method using the object
obj.greet()  # Output: Good morning!

# Static methods can also be called using the class name
Employee.greet()  # Output: Good morning!
