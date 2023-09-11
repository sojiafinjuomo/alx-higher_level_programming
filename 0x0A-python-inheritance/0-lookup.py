#!/usr/bin/python3
"""defines a lookup function"""


def lookup(obj):
    """returns the list of available attributes and methods of obj object"""
    a = dir(obj)
    return a
