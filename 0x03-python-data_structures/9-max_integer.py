#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    if my_list:
        n = my_list[0]
        for i in my_list:
            if n < i:
                n = i
            print(n)
