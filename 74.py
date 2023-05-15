def coin_change(coins, amount):
    # Initialize a table to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (amount + 1)
    
    # There are 0 coins needed to make an amount of 0
    dp[0] = 0
    
    # Compute the minimum number of coins needed for each amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return the minimum number of coins needed for the given amount
    if dp[amount] == float('inf'):
        return -1  # No solution found
    else:
        return dp[amount]


# Example usage
coins = [1, 2, 5]
amount = 11
result = coin_change(coins, amount)
print("Minimum number of coins
