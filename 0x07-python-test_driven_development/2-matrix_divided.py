#!/usr/bin/python3
"""
A function that divides all elements of a matrix.


"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Parameters:
    - matrix (list of lists): Matrix to be divided.
    - div (int or float): Number to divide the matrix elements by.

    Raises:
    - TypeError: If matrix is not a list of lists of integers or floats,
                 if each row of the matrix does not have the same size,
                 or if div is not a number.
    - ZeroDivisionError: If div is equal to 0.

    Returns:
    - list of lists: New matrix with elements divided by div,
    rounded to 2 decimal places.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        + "of integers/floats")

    if not all(isinstance(row, (list)) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")
    if not all(
        isinstance(element, (int, float))
        for row in matrix
        for element in row
            ):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
