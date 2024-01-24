#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print elememts of list

    Args:
        my_list (list): list to print from.
        x (int): number of elements to print.

    Returns:
        number of elements printed
    """
    node = 0
    for index in range(x):
        try:
            print("{}".format(my_list[index]), end="")
            node += 1
        except IndexError:
            break
    print("")
    return (node)
