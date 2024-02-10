#!/usr/bin/python3
"""Defines a square that inherits fro m rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square class

    Args:
        size (int): attributes of a square
    """

    def __init__(self, size):
        """Initializes an instance of a square
        Args:
            size (int): attributes of a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
