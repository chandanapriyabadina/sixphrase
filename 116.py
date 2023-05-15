import math

def chess_promotion():
    total_ways = math.comb(4, 1)
    return total_ways

# Call the function to get the number of ways for promotion
ways = chess_promotion()

print("Number of ways to promote a pawn:", ways)
