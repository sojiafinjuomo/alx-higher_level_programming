#!/usr/bin/python3
"""define function"""


def is_kind_of_class(obj, a_class):
    """
    if the object is an instance of, or
    if the object is an inherited instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
