def compute_f(n):
    if n == 0:
        return 1
    else:
        return compute_f(n-1) + 100

