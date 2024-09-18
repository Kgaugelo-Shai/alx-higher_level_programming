#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy_matrix = matrix.copy()

    for line in range(len(matrix)):
        cpy_matrix[line] = list(map(lambda x: x**2, matrix[line]))

    return (cpy_matrix)
