#!/usr/bin/python3
def print_matrix_integer(matrix=None):
    if matrix:
        for row in matrix:
            for column in row:
                print("{:d}".format(column), end=" ")
            print()  # Move to a new line after each row
