#!/usr/bin/python3
"""Defines a class Base-Geometry"""


class BaseGeometry:
    """base geometry representation"""
    def area(self):
        """method not defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (str): variable that stores the value
            value (int): parameter to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
