#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int or float): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square object with a given size.
        size (property): Retrieves the size of the square.
        size.setter: Sets the size of the square with validation checks.
        area(self): Calculates and returns the area of the square.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value (int or float): The size to set.

        Raises:
            TypeError: If the value is not a number.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares have the same area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two squares have different areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are different, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if the area of the first square is less than the area of the
        second square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the first square is less than the area
            of the second square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of the first square is less than or equal to the
        area of the second square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the first square is less than or
            equal to the area of the second square, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if the area of the first square is greater than the area
        of the second square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the first square is greater than
            the area of the second square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of the first square is greater than or equal
        to the area of the second square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the first square is greater than
            or equal to the area of the second square, False otherwise.
        """
        return self.area() >= other.area()
