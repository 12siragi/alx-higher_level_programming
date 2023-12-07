#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix with the same size as the input matrix
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # Compute the square value for each element in the input matrix
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[i][j] ** 2

    return result
