#!/usr/bin/python3
"""
A function that appends a string to a text file
"""


def append_write(filename="", text=""):
    """
    Calling the function
    """
    with open(filename, "a", encoding="UTF8") as w_f:
        return w_f.write(text)
