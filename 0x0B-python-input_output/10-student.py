#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """Represents a student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization of a student class

        Args:
            first_name (str): The first attribute
            last_name (str): second attribute
            age (int): third attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary rep. of Student

        Args:
            attrs (list): list of attributes
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
