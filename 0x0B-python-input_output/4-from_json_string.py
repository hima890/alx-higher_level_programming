#!/usr/bin/python3
"""Input output in python"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python
        data structure.

    Returns:
        object: The Python data structure represented by the JSON string.

    Example:
        s_my_list = "[1, 2, 3]"
        my_list = from_json_string(s_my_list)
        print(my_list)  # Output: [1, 2, 3]
    """
    import json
    return json.loads(my_str)
