# Accept input from the user
input_string = input("Enter the string: ")

# Initialize a dictionary to store letter frequencies
letter_freq = {}

# Count the frequencies of letters
for char in input_string:
    if char.isalpha():
