#!/usr/bin/python3
""""Input output in python"""


def read_file(filename=""):
    """
    Reads the contents of a text file and prints it to stdout.

    Args:
        filename (str, optional): The name of the text file to read.
        Defaults to "".

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.

    Note:
        This function assumes that the text file is encoded in UTF-8.

    Example:
        read_file("my_file.txt")
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
