#!/usr/bin/python3
#!/usr/bin/python3
"""
================================
module with method is_kind_of_class
================================
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance of the specified class,
        False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
