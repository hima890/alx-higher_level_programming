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

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid_idx = int(len(list_of_integers) / 2)

    if mid_idx != len(list_of_integers) - 1:
        if list_of_integers[mid_idx - 1] < list_of_integers[mid_idx] and\
           list_of_integers[mid_idx + 1] < list_of_integers[mid_idx]:
            return list_of_integers[mid_idx]
    else:
        if list_of_integers[mid_idx - 1] < list_of_integers[mid_idx]:
            return list_of_integers[mid_idx]
        else:
            return list_of_integers[mid_idx - 1]

    if list_of_integers[mid_idx - 1] > list_of_integers[mid_idx]:
        a_list = list_of_integers[0:mid_idx]
    else:
        a_list = list_of_integers[mid_idx + 1:]

    return find_peak(a_list)
