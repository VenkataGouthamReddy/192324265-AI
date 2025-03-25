# Initialize two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1 | set2
print("Union of set1 and set2:", union_set)

# Intersection of sets
intersection_set = set1 & set2
print("Intersection of set1 and set2:", intersection_set)

# Difference of sets
difference_set = set1 - set2
print("Difference of set1 and set2 (set1 - set2):", difference_set)

# Symmetric difference of sets
symmetric_difference_set = set1 ^ set2
print("Symmetric difference of set1 and set2:", symmetric_difference_set)

# Adding an element to set1
set1.add(9)
print("Set1 after adding 9:", set1)

# Removing an element from set2
set2.remove(8)
print("Set2 after removing 8:", set2)

# Checking membership
is_member = 3 in set1
print("Is 3 in set1:", is_member)

# Iterating through a set
print("Elements in set1:")
for element in set1:
    print(element, end=" ")
print()

# Set comprehension (creating a new set with squares of elements in set1)
squares_set = {x ** 2 for x in set1}
print("Set of squares of elements in set1:", squares_set)
