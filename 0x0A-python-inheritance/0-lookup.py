#!/usr/bin/python3
"""Fuction that returns all attributes of an object"""


def lookup(obj):
    """Returns list of all available attributes"""
    return (dir(obj))
