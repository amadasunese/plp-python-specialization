# Create an empty list called my_list.
my_empty_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
my_empty_list.extend([10, 20, 30, 40])
print(my_empty_list)

# Insert the value 15 at the second position in the list.
my_empty_list.insert(1, 15)
print(my_empty_list)

# Extend my_list with another list: [50, 60, 70].
my_empty_list.extend([50, 60, 70])
print(my_empty_list)

# Remove the last element from my_list.
my_empty_list.pop()
print(my_empty_list)

# Sort my_list in ascending order.
my_empty_list.sort()
print(my_empty_list)

# Find and print the index of the value 30 in my_list.
index_of_30 = my_empty_list.index(30)
print(index_of_30)
