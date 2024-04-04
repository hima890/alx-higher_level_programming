#!/usr/bin/python3
"""
Defines a add_integer function and use the test case for it


"""

def add_integer(a, b=98):
    """
    This is a semple adding function to add two integer value.
    check for the parameters types if not integer or float

    Parameters:
    - a (int or float) : First parameter
    - b (int or float) : Second parameter, defaults to 98

    Returns:
    - int: The sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
