# 'break' is used to come out of the loop when encountered.

for i in range(100):
    if(i == 34):
        break # exit the loop right now
    print(i)

# 'continue' is used to stop the current iteration of the loop and continue with the next one.  
  
for i in range(100):
    if(i == 34):
        continue # Skip this iteration  and continue rest of iteration
    print(i)

# pass is a null statement in python.
# It instructs to “do nothing”
l = [1,7,8]
for item in l:
    pass # without pass, the program will throw an error