#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for rw in range(len(matrix)):
            for col in range(len(matrix[rw])):
                if col != len(matrix[rw]) - 1:
                    edge = ' '
                else:
                    edge = ''
                print("{:d}".format(matrix[rw][col]), end=edge)
            print()
