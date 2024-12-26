# A set is a collection of unique and unordered elements
s = {1, 2, 72, 54, 2, 2, "Harsh"}  # Duplicates are automatically removed
print(s, type(s))  # Output: {1, 2, 72, 54, 'Harsh'} <class 'set'>

# Adding an element to the set
s.add(566)  # Adds 566 to the set
print(s)  # Output: {1, 2, 72, 54, 'Harsh', 566}

# Important Set Methods:
# 1. .add() - Adds a single element to the set
s.add(999)
print(s)

# 2. .remove() - Removes a specific element (raises KeyError if not found)
s.remove(54)
print(s)  # Output: {1, 2, 72, 'Harsh', 566, 999}

# 3. .discard() - Removes an element (doesn't raise an error if not found)
s.discard(1000)  # No error, even if 1000 is not in the set
print(s)

# 4. .pop() - Removes a random element from the set
popped = s.pop()  # Randomly removes an element
print(popped)
print(s)

# 5. .clear() - Removes all elements from the set
s.clear()
print(s)  # Output: set()

# 6. .union() - Combines two sets, removing duplicates
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # Output: {1, 2, 3, 4, 5}
print(union_set)

# 7. .intersection() - Gets common elements between sets
intersection_set = set1.intersection(set2)  # Output: {3}
print(intersection_set)

# 8. .difference() - Gets elements present in one set but not the other
difference_set = set1.difference(set2)  # Output: {1, 2}
print(difference_set)

difference_set = set2.difference(set1)  # Output: {4, 5}
print(difference_set)

# 9. .isdisjoint() - Checks if two sets have no common elements
print(set1.isdisjoint(set2))  # Output: False (since they share {3})
