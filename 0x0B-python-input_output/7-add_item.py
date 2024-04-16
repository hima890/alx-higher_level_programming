#!/usr/bin/python3
"""Input output in python"""


import sys
from os import path


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


# Filename for the JSON file
filename = "add_item.json"

# Check if the file exists, if not create it
if not path.exists(filename):
    save_to_json_file([], filename)

# Load the existing list from the file
my_list = load_from_json_file(filename)

# Add arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
