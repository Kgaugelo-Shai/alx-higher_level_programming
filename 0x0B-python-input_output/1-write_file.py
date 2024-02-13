#!/usr/bin/python3
"""This is a file-writing fuction."""


def write_file(filename="", text=""):
    """Write UTF8 text file from a string.

    Args:
        filename (str): name of file to write.
        text (str): text to write.
    Returns:
        number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as fd:
        return fd.write(text)
