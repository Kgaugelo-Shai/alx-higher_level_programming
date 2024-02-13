#!/usr/bin/python3
"""This is a JSON reading function."""
import json


def load_from_json_file(filename):
    """Python object from JSON."""
    with open(filename) as fd:
        return json.load(fd)
