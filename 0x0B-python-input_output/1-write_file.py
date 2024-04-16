#!/usr/bin/python3
"""Input output in python"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of
    characters written.

    Args:
        filename (str): The name of the text file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.

    Example:
        nb_characters = write_file("my_first_file.txt",
        "This School is so cool!\n")
        print(nb_characters)  # Output: 29
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
