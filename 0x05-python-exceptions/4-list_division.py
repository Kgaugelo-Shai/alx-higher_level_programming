def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists by the element.

    Args:
        my_list_1 (list): first list.
        my_list_2 (list): second list.
        list_length (int): number of elements.

    Returns:
        new list of length containing all divisions.
    """
    list_new = []
    for idx in range(0, list_length):
        try:
            ans = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            ans = 0
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        except IndexError:
            print("out of range")
            ans = 0
        finally:
            list_new.append(ans)
    return (list_new)
