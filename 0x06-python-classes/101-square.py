#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class."""
        self.size = size
        self.position = position

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
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)

    def __str__(self):
        """Returns a string representation of the square."""
        square_lines = []
        if self.size == 0:
            return ""

        for _ in range(self.position[1]):
            square_lines.append("\n")

        for _ in range(self.size):
            square_lines.append(" " * self.position[0] + "#" * self.size)

        return "\n".join(square_lines)
