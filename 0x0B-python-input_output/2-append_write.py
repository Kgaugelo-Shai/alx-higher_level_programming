#!/usr/bin/python3
"""This is a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a file.

    Args:
        filename (str): name of the file to append.
        text (str): string to append.
    Returns:
        number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
