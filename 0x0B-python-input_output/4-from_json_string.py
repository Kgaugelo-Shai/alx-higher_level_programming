#!/usr/bin/python3
"""This is a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returns a Python object of a JSON string."""
    return json.loads(my_str)
