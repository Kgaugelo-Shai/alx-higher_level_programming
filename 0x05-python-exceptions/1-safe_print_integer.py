#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer

    Args:
        value (int): integer to print

    Returns:
        TypeError or ValueError - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
