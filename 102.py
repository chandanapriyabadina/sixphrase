# Accept input from the user
input_string = input("Enter the string: ")
width = int(input("Enter the width: "))

# Initialize an empty result string
result = ""

# Iterate over the characters in the input string
for i, char in enumerate(input_string):
    result += char

    # Check if the width is reached
    if (i + 1) % width == 0:
        result += " "

# Print the wrapped paragraph
print("Wrapped paragraph:")
print(result)
