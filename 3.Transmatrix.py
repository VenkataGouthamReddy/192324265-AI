# Initialize a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Initialize result matrix with zeros
transpose = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Transpose the matrix
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i] = matrix[i][j]

# Print the transposed matrix
for row in transpose:
    print(row)
