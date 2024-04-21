#!/usr/bin/python3
"""
================================
module with method 10-square
================================
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square instance with size.

        Args:
            size (int): The size of the square.
        """
        self.__size = 0
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2
