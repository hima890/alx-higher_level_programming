#!/usr/bin/python3
"""Input output in python"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary representing the object in a serializable format.

    Example:
        m = MyClass("John")
        mj = class_to_json(m)
        print(mj)  # Output: {'name': 'John', 'number': 89}
    """
    json_dict = {}
    for attr, value in obj.__dict__.items():
        # Check if the attribute value is a serializable type
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
