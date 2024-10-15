#!/usr/bin/python3
"""Returns a dictionary description for a class to JSON object"""


def class_to_json(obj):
    """JSON serialization to a object

    Args:
        obj (any): instance of a class

    Returns:
       - a dictionary description of a class
    """
    return obj.__dict__
