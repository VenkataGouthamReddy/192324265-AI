# Initialize a list
my_list = [1, 2, 3]

# Append method
my_list.append(4)  # Adds 4 to the end of the list
print("List after append:", my_list)

# Extend method
my_list.extend([5, 6])  # Adds multiple elements to the end of the list
print("List after extend:", my_list)

# Add method (concatenation)
my_list += [7, 8]  # Concatenates another list to the original list
print("List after add (concatenation):", my_list)

# Delete elements using 'del' statement
del my_list[1]  # Deletes element at index 1
print("List after deleting index 1 using 'del':", my_list)

# Delete elements using 'remove()' method
my_list.remove(6)  # Removes the first occurrence of value 6
print("List after removing value 6 using 'remove()':", my_list)

# Delete elements using 'pop()' method
popped_element = my_list.pop()  # Removes the last element
print("List after popping the last element:", my_list)
print("Popped element:", popped_element)
