#!/usr/bin/python3
def no_c(my_string):
    str_copy = ""
    for byte in my_string:
        if byte != 'c' and byte != 'C':
            str_copy += byte
    return str_copy
