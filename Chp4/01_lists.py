# A list can hold multiple items of different data types
friends = ["apple", "orange", "banana", 7, False, "Akash"]  

# Accessing elements using their index (starting from 0)
print(friends[1])

# Lists are mutable, so we can change elements
friends[1] = "grapes"  # Changing 'orange' to 'grapes'

print(friends[1])
print(friends[1:4]) #list slicing 

# Example of a few operations:
friends.append("mango")  # Adding a new item to the list
print(friends) 

value= friends.pop(2)  # deletes the item from  list according to its index and returns the value
print(value)
print(friends) 

# Check length of the list
print(len(friends))

l1 = [1,23,34,4,434,3,45]

l1.sort() # Sorts the list 
print(l1)

l1.reverse() # Reverses the list 
print(l1)

l1.insert(3,81) # Insert 8 such that its index in the list is 3
print(l1)

l1.remove(81) # Removes 81 from the list 
print(l1)

