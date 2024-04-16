#!/usr/bin/python3
"""Input output in python"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the text file to write to.

    Returns:
        None

    Example:
        my_list = [1, 2, 3]
        save_to_json_file(my_list, "my_list.json")
    """
    import json
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
