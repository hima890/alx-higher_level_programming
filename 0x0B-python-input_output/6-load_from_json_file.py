#!/usr/bin/python3
"""Input output in python"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The Python object represented by the JSON data in the file.

    Example:
        my_list = load_from_json_file("my_list.json")
    """
    import json
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
