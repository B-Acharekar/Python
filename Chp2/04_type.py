# type() function : It is used to find the data type of a given variable in Python.
a = 31
t = type(a) #class <int>
print(t)

b = "Hello World"
t = type(b) #class <str>
print(t)

#typecasting : It is used to convert the data type of a given variable
c = "32.2"
d = float(c) # a but the type should be float
t = type(d)
print(t)

# str(31) =>"31"  integer to string conversion
# int("32") => 32  string to integer conversion
# float(32) => 32.0  integer to float conversion