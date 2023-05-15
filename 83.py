def fibonacci_sequence(n):
    sequence = []
    if n >= 0:
        sequence.append(0)
    if n >= 1:
        sequence.append(1)

    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence

# Read input from the console
