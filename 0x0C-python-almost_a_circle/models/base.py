#!/usr/bin/python3
"""Defines a base class model"""
import json


class Base:
    """This class will be the base of all other classes in this project

    Private Class Attributes:
        __nd_object (int): The number of bases instantiated
    """

    __nb_object = 0

    def __init__(self, id=None):
        """This instantiates a new Base object

        Args:
            id (int): unique identity of the new Base object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): This is a list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
