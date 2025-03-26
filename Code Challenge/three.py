# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console

person = dict() # or person = {}

# Input name and assign to key
name = input("What is your name: ")
person['name'] = name

# Input age and assign to key
age = input("What is your age: ")
person['age'] = age

# Input color and assign to key
colour = input("What is your favorite colour: ")
person['color'] = colour

print(f"Person dictionary: {person}") # Output