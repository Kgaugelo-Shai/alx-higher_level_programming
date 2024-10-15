#!/usr/bin/python3
"""This is a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return JSON representation of a string."""
    return json.dumps(my_obj)
