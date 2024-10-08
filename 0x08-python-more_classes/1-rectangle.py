#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """ represents a rectangle"""
    
    def __init__(self, width=0, height=0):
        """Initializes the rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: when values are not integers
            ValueError: when value is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns the width """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns the height """
        return self.__height

    @height.setter
    def height(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
