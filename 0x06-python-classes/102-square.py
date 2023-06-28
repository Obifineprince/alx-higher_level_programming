#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class."""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.size ** 2

    def __eq__(self, other):
        """Equality comparison operator."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Inequality comparison operator."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than comparison operator."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Less than or equal to comparison operator."""
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        """Greater than comparison operator."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Greater than or equal to comparison operator."""
        return self.__gt__(other) or self.__eq__(other)
