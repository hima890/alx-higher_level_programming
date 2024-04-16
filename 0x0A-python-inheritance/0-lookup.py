#!/usr/bin/python3
"""
Get the object attributes and methods
"""


def lookup(obj):
    """
    Function to get all object attributes and methods,
    using the dir method

    Args:
    obj: Python object

    Return: A list content all the attributes and methods
    """
    return list(dir(obj))
