#!/usr/bin/python3
"""This class inherits from class list"""


class MyList(list):
    """defines a list class"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
