#!/usr/bin/python3
"""
================================
module with method 100-my_int
================================
"""


class MyInt(int):
    """
    MyInt class, inherits from int but overrides == and != operators.
    """

    def __eq__(self, other):
        """
        Overrides the == operator to return the opposite result.

        Args:
            other (int): The value to compare with.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to return the opposite result.

        Args:
            other (int): The value to compare with.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)
