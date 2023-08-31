#!/usr/bin/python3
"""defines a class"""


class Square:
    """class named Square"""

    def __init__(self, size=0):
        """initializes a private attribute

        Args:
            size(int): size of the side of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """defines area of a square"""
        return(self.__size * self.__size)
