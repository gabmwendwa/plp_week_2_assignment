# Create an empty list called my_list.
my_list = []
print(f"Empty list: {my_list}")

# Append the following elements to my_list: 10, 20, 30, 40.
nums = [10, 20, 30, 40]
for num in nums:
    my_list.append(num)
print(f"Appended list: {my_list}")

# Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print(f"Inserted list: {my_list}")

# Extend my_list with another list: [50, 60, 70].
another_list = [50, 60, 70]
my_list.extend(another_list)
print(f"Extnded list: {my_list}")

# Remove the last element from my_list.
del my_list[-1]
print(f"Removed list: {my_list}")

# Sort my_list in ascending order.
my_list.sort()
print(f"Sorted list: {my_list}")

# Find and print the index of the value 30 in my_list.
i = my_list.index(30)
print(f"Found in list: {i}")
