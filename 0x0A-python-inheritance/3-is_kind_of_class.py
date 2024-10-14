#!/usr/bin/python3
"""Defines a function to check for class instances"""


def is_kind_of_class(obj, a_class):
    """checks object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class

    Args:
        obj (any): the object to check
        a_class (type): the class to check if the object is an instance of

    Returns:
        True - if obj is an instance of a_class
        False -  otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
