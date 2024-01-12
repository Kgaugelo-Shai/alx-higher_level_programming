#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = a_dictionary.copy()
    key_ls = list(nd.keys())

    for c in key_ls:
        nd[c] *= 2

    return (nd)
