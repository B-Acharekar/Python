# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class demo:
    a = 4

obj = demo()
print(obj.a)
obj.a = 0
print(obj.a)
print("Class attribute a: ", demo.a)  # Output: 4