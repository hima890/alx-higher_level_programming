#!/usr/bin/python3
"""
================================
module with method 4-inherits_from
================================
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of a class that inherited
        from the specified class; otherwise False.
    """
    # Base case: if the object's class is the specified class, return True
    if type(obj) == a_class:
        return True
    for base_class in type(obj).__bases__:
        if inherits_from(base_class, a_class):
            return True
    # If no base class matches a_class, return False
    return False
