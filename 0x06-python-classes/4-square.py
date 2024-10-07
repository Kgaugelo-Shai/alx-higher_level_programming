#!/usr/bin/python3

"""This defines a class Square."""


class Square:
    """Representation a square object."""

    def __init__(self, size=0):
        """This initializes a new square object.

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the current size of a square object."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square observed."""
        return (self.__size * self.__size)
