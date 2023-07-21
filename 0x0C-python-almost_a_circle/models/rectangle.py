#!/usr/bin/python3
"""
File: rectangle.py
Desc: This module contains a class, Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle object.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        Returns a string representation of the Rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def check_value(self, name, value, sides=True):
        """
        Checks if the correct input was inserted for width, height, x, and y attributes.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if sides:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        elif value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """
        Getter for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value for the width attribute.
        """
        self.check_value('width', value)
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value for the height attribute.
        """
        self.check_value('height', value)
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the value for the x attribute.
        """
        self.check_value('x', value, False)
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value for the y attribute.
        """
        self.check_value('y', value, False)
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle instance with the character '#'.
        """
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print((' ' * self.__x) + ('#' * self.__width) + '\n', end='')

    def update(self, *args, **kwargs):
        """
        Updates the attribute values.
        """
        if len(args):
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.width = arg
                elif n == 2:
                    self.height = arg
                elif n == 3:
                    self.x = arg
                elif n == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Returns the dictionary representation of the class.
        """
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
