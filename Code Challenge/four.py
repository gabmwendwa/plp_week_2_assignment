# Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

# User input first set
A = set(input("Enter first set: "))
print(f"The first set: {A}\n") # Output

# User input second set
B = set(input("Enter second set: "))
print(f"The second set: {B}\n") # Output

# User input first set
C = A.intersection(B)
print(f"The common elements: {C}\n") # Output
print(f"The common elements: {A & B}\n") # Output
