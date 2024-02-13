#!/usr/bin/python3
"""This is a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to text file using JSON."""
    with open(filename, "w") as fd:
        json.dump(my_obj, fd)
