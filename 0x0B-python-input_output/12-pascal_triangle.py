#!/usr/bin/python3
"""Input output in python"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = []
    for row in range(n):
        current_row = [1] * (row + 1)
        for col in range(1, len(current_row) - 1):
            value1 = triangle[row - 1][col]
            value2 = triangle[row - 1][col - 1]
            current_row[col] = value1 + value2

        triangle.append(current_row)

    return triangle
