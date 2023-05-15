numbers = [2, 4, 6, 8]

for num in numbers:
    assert num % 2 == 0, "Number {} is not even.".format(num)

print("All numbers are even.")
