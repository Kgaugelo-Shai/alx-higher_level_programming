#!/usr/bin/python3

"""Definition of class Square."""


class Square:
    """Represents a square object."""

    def __init__(self, size=0):
        """Initializes a new Square object.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
