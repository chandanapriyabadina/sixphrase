def solve_puzzle(heads, legs):
    for c in range(heads + 1):
        r = heads - c
        if 2 * c + 4 * r == legs:
            return c, r
    return None

# Given information
total_heads = 35
total_legs = 94

# Solve the puzzle
solution = solve_puzzle(total_heads, total_legs)

# Print the solution
if solution
