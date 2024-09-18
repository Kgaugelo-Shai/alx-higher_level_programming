#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    key_ls = list(a_dictionary.keys())

    for i in key_ls:
        count += 1

    return (count)
