# Object-oriented programming (OOP) involves solving problems by creating objects, 
# which are instances of classes. A class defines a blueprint or template, and 
# memory is allocated only when an object is created.

class Employee:
    # Class attributes
    name = "Yash"
    language = "Java"
    salary = "500000"

# Creating an object (instantiation of the class)
my_obj = Employee()

# Accessing and modifying class attributes using the object
print(my_obj.name)  # Output: Yash
my_obj.name = "John"  # Modifying the name attribute for this object
print(my_obj.name)  # Output: John

# Adding an instance attribute
my_obj.role = "Jr. Developer"  # Instance-specific attribute
print(my_obj.role)  # Output: Jr. Developer

# Creating another object
my_obj2 = Employee()
# print(my_obj2.role)  # Uncommenting this will cause an AttributeError
# Because 'role' is not defined in the class or for this specific object

