n = int(input("Enter the value of n: "))  # Read the value of n from the console

sum = 0.0
for i in range(1, n + 1):
    sum += i / (i + 1)

print("The sum is:", round(sum, 2))
