def even_numbers(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

# Read input from the console
n = int(input("Enter a value for n: "))

# Generate the even numbers
even_nums = even_numbers(n)

# Print the even numbers in comma-separated form
result = ",".join(str(num) for num in even_nums)
print(result)
