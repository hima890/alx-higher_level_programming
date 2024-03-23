#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    This a simple class to demonstrate documentation of classes in python
    incilding attributes and functions and more using the beast stander.

    Attributes:
        - size: Un Intger attribute
    """

    def __init__(self, size=0):
        """
        Constructor for Square.

        Parameters:
        - size (str): Value for size.
        """

        self.__size = size

    def area(self):
        """
        Public instance method: def area(self):
        that returns the current square area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if not value >= 0:
            raise ValueError("size must be >= 0")
        self.__size = value
