#!/usr/bin/python3
"""The class Rectangle inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherites form baseclass BaseGeometry"""

    def __init__(self, width, height):
        """initializes the objects"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
