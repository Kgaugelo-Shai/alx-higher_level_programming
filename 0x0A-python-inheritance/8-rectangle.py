#!/usr/bin/python3
"""Defines a rectangle class that inherits from base geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle"""

    def __init__(self, width, height):
        """initializes a rectangle class
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
