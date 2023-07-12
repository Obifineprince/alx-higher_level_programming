#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class."""
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Computes the area of the square."""
        return self.__size ** 2
