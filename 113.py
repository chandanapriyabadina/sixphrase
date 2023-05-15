def egg_drop(num_eggs, num_floors):
    # Create a 2D array to store the minimum attempts for each number of eggs and floors
    dp = [[0] * (num_floors + 1) for _ in range(num_eggs + 1)]
    
    # Base cases:
    # If there are no floors, no attempts are needed
    # If there is only one floor, one attempt is needed
    for egg in range(1, num_eggs + 1):
        dp[egg][0] = 0
        dp[egg][
