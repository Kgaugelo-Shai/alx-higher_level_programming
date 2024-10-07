#!/usr/bin/python3
"""matrix division function."""


def matrix_divided(matrix, div):
    """Divide elements of a matrix.

    Args:
        matrix (list): list of lists of ints or floats.
        div (int/float): divisor.
    Raises:
        TypeError: If matrix contains non-numbers.
        TypeError: If matrix contains rows of different sizes.
        TypeError: If div is not int or float.
        ZeroDivisionError: div is 0.
    Returns:
        new matrix representing result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(r, list) for r in matrix) or
            not all((isinstance(e, int) or isinstance(e, float))
                    for e in [num for r in matrix for num in r])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x1: round(x1 / div, 2), r)) for r in matrix])
