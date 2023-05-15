import random

random_numbers = []
while len(random_numbers) < 5:
    num = random.randint(1, 1000)
    if num % 5 == 0 and num % 7 == 0:
        random_numbers.append(num)

print("Random numbers divisible by 5 and 7 between 1 and 1000:", random_numbers)
