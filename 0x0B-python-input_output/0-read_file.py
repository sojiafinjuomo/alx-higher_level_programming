#!/usr/bin/python3
"""
function that reads a text file and prints it to stdout:
"""


def read_file(filename=""):
    """calling the function"""
    with open(filename, encoding="UTF-8") as readfile:
        print(readfile.read(), end="")
