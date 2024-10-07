#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer.

    ValueError message is caught,
    message is printed to standard error.

    Args:
        value (int): integer to print.

    Returns:
        TypeError or ValueError - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
