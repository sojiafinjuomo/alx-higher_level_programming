#!/usr/bin/python3
"""defines a Rectangle class"""


class Rectangle:
    """class named Rectangle"""

    def __init__(self, width=0, height=0):
        """initializes width and height attributes.

        Args:
            width(int): width of Rectangle
            height(int): heigth of Rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """property/method that retrieves width"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """property/method to retrieve value of height"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
