#!/usr/bin/python3
"""defines a class"""


class Square:
    """class named Square"""

    def __init__(self, size=0):
        """initializes a private attribute

        Args:
            size(int): size of sides of square
        """
        self.size = size

    @property
    def size(self):
        """method that retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """method checks the state of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """defines area of a square"""
        return (self.__size * self.__size)
