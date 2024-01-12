#!/usr/bin/python3
def uniq_add(my_list=[]):
    node = set(my_list)
    count = 0

    for line in node:
        count += line

    return (count)
