#!/usr/bin/python3
"""
Class MyList that inherits of list
"""


class MyList(list):
    """
    Class MyList prints the list, but sorted
    (ascending sort)

    Attributes:
    element(int) : Element to be add to the list
    """
    pass

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)

        Args:
        element(int) : Element to be add to the list

        Return: A sorted (ascending sort) list
        """
        # if not self:
        #     raise ValueError("List is empty")

        # for ele in self:
        #     if type(ele) != int:
        #         raise TypeError("List elemnts must be intgers")
        #     break

        print(list(sorted(self)))
