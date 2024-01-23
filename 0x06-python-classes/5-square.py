#!/usr/bin/python3

"""This defines a class Square."""


class Square:
    """this represent a square object."""

    def __init__(self, size):
        """this will initialize a new square.

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square observed."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square observed."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square with # characters to stdio."""
        for index in range(0, self.__size):
            [print("#", end="") for i in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
