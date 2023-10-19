#!/usr/bin/python3
"""function returns true or false"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an
    instance of the specified class ; otherwise False.
    Args:
        obj(any):the object to check
        a_class(type): the one to be compared
    Returns: True or False
    """
    if type(obj) == a_class:
        return True
    return False
