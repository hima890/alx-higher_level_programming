#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    This a simple class to demonstrate documentation of classes in python
    incilding attributes and functions and more using the beast stander.

    Attributes:
        - size: Un Intger attribute
    """

    def __init__(self, size):
        """
        Constructor for Square.

        Parameters:
        - size (str): Value for size.
        """

        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if not self.__size >= 0:
            raise ValueError("size must be >= 0")
