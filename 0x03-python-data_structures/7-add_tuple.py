#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_len, b_len = len(tuple_a), len(tuple_b)
    tuple_new = ((tuple_a[0] if a_len >= 1 else 0) +
                 (tuple_b[0] if b_len >= 1 else 0),
                 (tuple_a[1] if a_len >= 2 else 0) +
                 (tuple_b[1] if b_len >= 2 else 0))
    return tuple_new
