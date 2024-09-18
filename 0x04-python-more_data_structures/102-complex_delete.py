#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_ls = list(a_dictionary.keys())

    for val in keys_ls:
        if value == a_dictionary.get(val):
            del a_dictionary[val]

    return (a_dictionary)
