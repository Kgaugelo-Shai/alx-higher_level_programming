#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    count = 0
    divisor = 0

    for tup in my_list:
        count += tup[0] * tup[1]
        divisor += tup[1]

    return (count / divisor)
