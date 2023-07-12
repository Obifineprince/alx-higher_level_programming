#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class."""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter method to retrieve the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position attribute."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Computes the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
