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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string represenation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherits base.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as j_file:
            if list_objs is None:
                j_file.write("[]")
            else:
                list_dict = []
                for ob in list_objs:
                    list_dict.append(ob.to_dictionary())
                j_file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of the JSON string representation json_string

        Args:
            json_string (str): s a string representing a list of dictionaries

        Returns:
            - If json_string is None or empty, return an empty list
            - Otherwise, return the list represented by json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all atttibutes already set

        Args:
            **dictionary (dict): a pointer to a dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                temp = cls(1, 1)
            elif cls.__name__ == "Square":
                temp = cls(1)
            temp.update(**dictionary)
            return temp

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances created from JSON file

        Returns:
            if the file does not exist - an empty list
            Otherwise - a list of the instantiated classes
        """
        filename = cls.__name__ + ".json"
        with open(filename, "r") as j_file:
            list_dict = Base.from_json_string(j_file.read())

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set

        Args:
            **dictionary (dict): key/value pairs to instantiate object with
        """
        if dictionary and dictionary != []:
            if cls.__name__ == "Rectangle":
                new_base = cls(1, 1)
            elif cls.__name__ == "Square":
                new_base = cls(1)
            new_base.update(**dictionary)
            return new_base

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances

        Reads the file cls.__name__.json

        Returns:
            - a list of instances on success
            - otherwise, an empty list
            """

        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as j_file:
                dict_ls = Base.from_json_string(j_file.read())
                new = []
                for ele in dict_ls:
                    new.append(cls.create(**ele))
                return new
        except IOError:
            return []
