#!/usr/bin/python3
"""
================================
module with method 11-square
================================
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.

        Returns:
            None
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string representation of the Square.
        """
        return "[Square] {}/{}".format(self.width, self.height)

    def area(self):
        """
        Calculates the area of the Square.

        Returns:
            int: The area of the Square.
        """
        return self.width * self.height
