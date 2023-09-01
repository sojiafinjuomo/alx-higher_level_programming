#!/usr/bin/python3
"""defines a class"""


class Square:
    """class named Square"""

    def __init__(self, size=0):
        """initializes an attribute

        Args:
            size(int): size of sides of square
        """
        self.size = size

    @property
    def size(self):
        """property/method that retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """defines area of a square"""

        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
