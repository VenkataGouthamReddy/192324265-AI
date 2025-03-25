# Define nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested List:", nested_list)

# Find length of the list
length = len(nested_list)
print("Length of the nested list:", length)

# Concatenate lists
list1 = [10, 11, 12]
list2 = [13, 14, 15]
concatenated_list = list1 + list2
print("Concatenated List:", concatenated_list)

# Check membership
element = 10
is_member = element in concatenated_list
print(f"Is {element} in concatenated list:", is_member)

# Iterate through the list
print("Iteration through concatenated list:")
for item in concatenated_list:
    print(item, end=" ")
print()

# Indexing
index = 2
indexed_element = concatenated_list[index]
print(f"Element at index {index}:", indexed_element)

# Slicing
sliced_list = concatenated_list[1:4]
print("Sliced List (from index 1 to 3):", sliced_list)
