#!/usr/bin/python3
"""
File: base.py
Desc: THis module contains a class; Base
"""

import csv
import random
import json
import turtle

# models/__init__.py
# Create an empty file

# models/base.py
class Base:
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id  # assign id if provided
        else:
            Base.__nb_objects += 1  # increment class attribute
            self.id = Base.__nb_objects
