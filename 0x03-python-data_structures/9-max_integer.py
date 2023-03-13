#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_int = my_list[0]
    for ints in my_list:
        if ints > max_int:
            max_ints = ints
