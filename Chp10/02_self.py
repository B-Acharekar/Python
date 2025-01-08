class Employee:
    # Class attributes
    name = "Yash"
    language = "Java"
    salary = "500000"

    # The `self` parameter refers to the specific instance of the class calling the method.
    # It is automatically passed when a method is called on an object.
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

# Creating an object of the Employee class
obj = Employee()

# Method 1: Calling the method using the object
obj.getInfo()  # Output: The language is Java. The salary is 500000

# Method 2: Calling the method using the class name
# When calling a method from the class directly, you need to explicitly pass the object
# as the first argument (replacing `self`).
Employee.getInfo(obj)  # Output: The language is Java. The salary is 500000
