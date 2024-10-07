#!/usr/bin/python3
"""matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply 2 matrices.

    Args:
        m_a (list of lists of ints/floats): first matrix.
        m_b (list of lists of ints/floats): second matrix.
    Raises:
        TypeError: either m_a or m_b is not a list of lists of ints/floats.
        TypeError: either m_a or m_b is empty.
        TypeError: either m_a or m_b has different-sized rows.
        ValueError: m_a and m_b cannot be multiplied.
    Returns:
        new matrix representing multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(r, list) for r in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(r, list) for r in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ell, int) or isinstance(ell, float))
               for ell in [num for r in m_a for num in r]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ell, int) or isinstance(ell, float))
               for ell in [num for r in m_b for num in r]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(r) == len(m_a[0]) for r in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(r) == len(m_b[0]) for r in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inver_b = []
    for row in range(len(m_b[0])):
        n_row = []
        for ch in range(len(m_b)):
            n_row.append(m_b[ch][row])
        inver_b.append(n_row)

    n_matrix = []
    for r in m_a:
        n_row = []
        for cl in inver_b:
            prd = 0
            for idx in range(len(inver_b[0])):
                prd += r[idx] * cl[idx]
            n_row.append(prd)
        n_matrix.append(n_row)

    return n_matrix
