#!/usr/bin/python3
"""
A function that print text with newlines.


"""


def text_indentation(text):
    """
    Print the input text with indentation based on punctuation marks.

    Parameters:
    - text (str): The input text to be printed.

    Raises:
    - TypeError: If text is not a string.

    Returns:
    - None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char in ('.', '?', ':'):
            print("\n\n", end="")
