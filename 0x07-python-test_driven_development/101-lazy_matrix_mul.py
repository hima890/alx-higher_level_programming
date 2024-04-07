#!/usr/bin/python3
"""
A function that multy two matrix using numpy.


"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
    - m_a (list of lists): First matrix
    - m_b (list of lists): Second matrix

    Returns:
    - np.ndarray: Resultant matrix

    Raises:
    - TypeError: If m_a or m_b is not a list of lists, or if elements are not integers or floats,
                 or if each row of m_a or m_b is not of the same size
    - ValueError: If m_a or m_b is empty
    - ValueError: If m_a and m_b can't be multiplied
    """
    try:
        result = np.matmul(np.array(m_a), np.array(m_b))
        return result
    except ValueError as ve:
        raise ValueError("m_a and m_b can't be multiplied") from ve
    except TypeError as te:
        if isinstance(m_a, list) and isinstance(m_b, list):
            raise TypeError("each element of m_a and m_b must be a list") from te
        else:
            raise TypeError("m_a and m_b must be a list of lists") from te
