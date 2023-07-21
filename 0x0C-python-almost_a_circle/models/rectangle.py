#!/usr/bin/python3
"""
File: rectangle.py
Desc: This module contains a class; Rectangle
"""

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
	super().__init__(id

    def __str__(self):
        """
        String representation of class
        """
        return ("[Rectangle] (" +
                str(self.id) + ") " + str(self.__x) + "/" + str(self.__y) +
                " - " + str(self.__width) + "/" + str(self.__height))

    def check_value(self, name, value, sides=True):
        """
        Checks if correct input was inserted
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if sides:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

   def area(self):
        """
        Returns the area of the rectangle
        """
        return (self.__width * self.__height)
   def display(self):
        """Display rectangle using '#' character"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
   def display(self):
        """Display rectangle using '#' character"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update rectangle attributes"""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
   def to_dictionary(self):
    """Returns the dictionary representation of the class"""
    d = {}
    d["id"] = self.id
    d["width"] = self.width
    d["height"] = self.height
    d["x"] = self.x
    d["y"] = self.y
    return d
