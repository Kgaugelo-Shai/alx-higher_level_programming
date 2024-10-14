#!/usr/bin/python3
"""Defines a class that inherits from int"""


class MyInt(int):
    """This inverts == and != operators"""

    def __eq__(self, value):
        """Override ==  with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != with == behavior."""
        return self.real == value
