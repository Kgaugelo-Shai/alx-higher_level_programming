#!/usr/bin/python3
"""This defines a square class that inherits from
   a rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """This initializes a square class

        Args:
            size (int): the dimensions of the square
            x (int): x coordinate of the square
            y (int): y cooordinate of the square
            id (int): The unique id of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.width = value

    def __str__(self):
        """Returns a string representation of a Square."""
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.width)
