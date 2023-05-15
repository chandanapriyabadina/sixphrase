# Read ASCII string from user
ascii_string = input("Enter an ASCII string: ")

# Convert ASCII string to UTF-8 encoded Unicode string
utf8_string = ascii_string.encode('utf-8')

# Print the UTF-8 encoded string
print("UTF-8 encoded string:", utf8_string)
