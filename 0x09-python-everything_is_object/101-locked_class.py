#!/usr/bin/python3
"""Definition of a locked class."""


class LockedClass:
    """
    Prevents user from instantiating new LockedClass attributes
    but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
