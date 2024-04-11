#!/usr/bin/python3
"""Defines a class implements a magic circle"""


import math


class MagicClass:
    """
    This class implements a magic circle.

    Methods:
        __init__(self, radius=0): Initializes a MagicClass object with a given
        radius.
        area(self): Calculates and returns the area of the magic circle.
        circumference(self): Calculates and returns the circumference of
        the magic circle.
    """
    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with a given radius.

        Args:
            radius (int or float): The radius of the magic circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
