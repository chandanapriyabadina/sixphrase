def print_string_with_max_length(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    
    if len1 > len2:
        print(str1)
    elif len2 > len1:
        print(str2)
    else:
        print(str1)
        print(str2)

# Example usage
string1 = "Hello"
string2 = "World!"
print_string_with_max_length(string1, string2)
