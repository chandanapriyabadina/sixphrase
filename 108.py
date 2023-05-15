def is_safe(board, row, col, N):
    # Check if a queen can be placed at the specified row and column
    # without conflicting with existing queens on the board
    
    # Check the row
    for c in range(col):
        if board[row][
