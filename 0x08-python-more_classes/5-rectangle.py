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

    def area(self):
        """defines area of a rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """defines perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        print() and str() should print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rec = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rec

    def __repr__(self):
        """
        return a string representation of the rectangle
        to recreate a new instance
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
