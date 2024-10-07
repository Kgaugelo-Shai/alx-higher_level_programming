#!/usr/bin/python3
"""square-printing function."""


def print_square(size):
    """Print square with # character.

    Args:
        size (int): height/width of square.
    Raises:
        TypeError: size is not integer.
        ValueError: size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for idx in range(size):
        [print("#", end="") for i in range(size)]
        print("")
