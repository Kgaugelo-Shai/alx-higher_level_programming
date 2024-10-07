#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        ans = a / b
    except (TypeError, ZeroDivisionError):
        ans = None
    finally:
        print("Inside result: {}".format(ans))
    return (ans)
