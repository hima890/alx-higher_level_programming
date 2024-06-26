#!/usr/bin/python3
"""
A function that print the full name.


"""


def say_my_name(first_name, last_name=""):
    """
    Print the full name based on the provided first and last names.

    Parameters:
    - first_name (str): The first name of the person.
    - last_name (str, optional): The last name of the person.
        Defaults to an empty string.

    Raises:
    - TypeError: If first_name is not a string or last_name is not a string.

    Returns:
    - None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
