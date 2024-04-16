#!/usr/bin/python3
"""Input output in python"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.

    Example:
        my_list = [1, 2, 3]
        s_my_list = to_json_string(my_list)
        print(s_my_list)  # Output: "[1, 2, 3]"
    """
    import json
    return json.dumps(my_obj)
