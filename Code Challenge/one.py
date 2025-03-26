# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

# Declare an empty list
num_list = list() # or []
# Declare total variable and initiate it with a value of 0
total = 0 

print("Enter four numbers below:") # instrustion for user input

# Loop four times to get user input
for i in range(4):
    num = int(input(f"Enter number {i+1}: ")) # store input in num variable
    print(f"You have entered: {num}") # Output
    num_list.append(num) # append num value to num_list
    total += num # add value of num to current total

print(f"The list is: {num_list}") # Output
print(f"The total of the list is: {total}") # Output
