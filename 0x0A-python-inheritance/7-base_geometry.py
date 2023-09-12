#!/usr/bin/python3
"""An empty class BaseGeometry"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented"

    def integer_validator(self, name, value):
        """function validates value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
