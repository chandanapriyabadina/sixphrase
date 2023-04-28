def even(x):
    return x%2==0
even numbers = filter(even,range(1,21))
print(list(even numbers))
