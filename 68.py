def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store the lengths of common substrings
    table = [[0] * (n + 1) for _ in range(m + 1)]

