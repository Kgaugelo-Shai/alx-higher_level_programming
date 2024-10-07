#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first n elements of a list.

    Args:
        my_list (list): list to print from.
        x (int): number of elements to print.

    Returns:
        number of elements printed
    """
    node = 0
    for idx in range(0, x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            node += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (node)
