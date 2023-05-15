def min_cost_path(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Create a table to store the minimum costs
    dp = [[0] * cols for _ in range(rows)]

    # Compute the minimum cost for the top-left cell
    dp[0][0] = grid[0][0]

    # Compute the minimum cost for the first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Compute the minimum cost for the first column
    for i in range(1, rows):
        dp[i][0
