#!/usr/bin/python3
"""
File: square.py
Desc: This module contains a class, Square, representing a square.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a specific type of rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the Square object.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Returns a string representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        Getter for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.
        """
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attribute values.
        """
        if len(args):
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.
        """
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
