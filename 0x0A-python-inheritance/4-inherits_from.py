#!/usr/bin/python3
"""Defines a function that checks for a subclass"""


def inherits_from(obj, a_class):
    """check if an object is an instance of a class
    that inherited (directly or indirectly)
    from a specified class

    Args:
        obj (any): the object to be tested
        a_class (type): the a_class the object is tested against

    Returns:
        True - is obj inherits from a a_class
        False - otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
