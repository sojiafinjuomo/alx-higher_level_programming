#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_my_list = len(my_list) - 1
    if idx < 0 or idx >= len_my_list:
        print(my_list)
    else:
        new_list = my_list.copy()
        new_list[idx] = element
    print(new_list)
    print(my_list)
