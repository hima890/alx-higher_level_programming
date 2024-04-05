#!/usr/bin/python3
"""
A function that printa Squer.


"""


def print_square(size):
    """
    Print a square made of '#' characters.

    Parameters:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer or if size is a float.
    - ValueError: If size is less than 0.

    Returns:
    - None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
