# Create a python program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

# Initialize list of words
my_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','aa', 'bbbb', 'cccccc']
print(f"The list of words: {my_list}\n") # Output

new_list = [word for word in my_list if len(word) % 2 != 0]
print(f"The new list of words with odd lenght count: {new_list}\n") # Output
