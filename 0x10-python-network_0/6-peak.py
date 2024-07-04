#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers.
A peak is an element which is greater than or equal to its neighbors.
"""


def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.

    A peak element is defined as an element that is greater than or equal to
    its immediate neighbors.
    For the elements at the ends of the list, we consider only one neighbor.

    Parameters:
    - list_of_integers (List[int]): The list of integers in which to
    find a peak.

    Returns:
    int or None: The value of the peak element if found, otherwise None.

    Example:
    >>> find_peak([1, 3, 4, 3, 5, 1])
    4
    >>> find_peak([])
    None
    """
    if not list_of_integers:
        return None

    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
