# Initialize the chessboard
n = 8  # Number of queens
board = [['.' for _ in range(n)] for _ in range(n)]

# Initialize helper lists to track columns and diagonals
columns = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)

# Start the column and solutions list
col = 0
solutions = []

# Backtracking logic
while col >= 0:
    row = 0
    found = False
    while row < n:
        if not columns[row] and not diag1[col - row + n - 1] and not diag2[col + row]:
            # Place the queen
            board[row][col] = 'Q'
            columns[row] = True
            diag1[col - row + n - 1] = True
            diag2[col + row] = True
            found = True
            break
        row += 1
    
    if found:
        if col == n - 1:
            # Solution found, add it to the solutions list
            solution = ["".join(board[i]) for i in range(n)]
            solutions.append(solution)
            # Remove the last queen to backtrack
            board[row][col] = '.'
            columns[row] = False
            diag1[col - row + n - 1] = False
            diag2[col + row] = False
            row += 1
        else:
            col += 1
    else:
        # Backtrack to previous column
        col -= 1
        if col >= 0:
            for r in range(n):
                if board[r][col] == 'Q':
                    board[r][col] = '.'
                    columns[r] = False
                    diag1[col - r + n - 1] = False
                    diag2[col + r] = False
                    row = r + 1
                    break

# Display all solutions
for solution in solutions:
    for row in solution:
        print(row)
    print()
