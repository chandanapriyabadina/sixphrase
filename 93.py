import random

random_divisible = random.choice([num for num in range(10, 151) if num % 5 == 0 and num % 7 == 0])
print("Random number divisible by 5 and 7 between 10 and 150:", random_divisible)
