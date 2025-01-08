class Employee:
    # Class attributes
    name = "Yash"
    language = "Java"
    salary = "500000"

    # __init__ is a special method, also known as a constructor
    # It is automatically called when an object of the class is created
    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("Employee object created")

    # Method to display the attributes of the Employee
    def display(self):
        print("Name:", self.name)
        print("Language:", self.language)
        print("Salary:", self.salary)


# Creating an object of the Employee class
obj = Employee("John","2500000","Python")  # This automatically calls the __init__ method

# Displaying the attributes of the object
obj.display()
