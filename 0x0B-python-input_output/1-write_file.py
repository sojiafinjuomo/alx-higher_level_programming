#!/usr/bin/python3
"""
A function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    writes a string
    """
    with open(filename, mode="w", encoding="UTF8") as w_f:
        return w_f.write(text)
