#!/usr/bin/python3

"""This defines a class Square."""


class Square:
    """Representation a square."""

    def __init__(self, size=0):
        """Initializes a new square object.

        Args:
            size (int): size of the new square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the square observed."""
        return (self.__size * self.__size)
