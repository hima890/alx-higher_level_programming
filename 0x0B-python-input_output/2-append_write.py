#!/usr/bin/python3
"""Input potput in python"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the
    number of characters added.

    Args:
        filename (str): The name of the text file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.

    Example:
        nb_characters_added = append_write("file_append.txt",
        "This School is so cool!\n")
        print(nb_characters_added)  # Output: 29
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added
