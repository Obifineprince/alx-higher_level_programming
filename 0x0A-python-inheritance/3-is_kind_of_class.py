#!/usr/bin/python3

"""
Desc: This module contains one function;
is_kind_of_class(obj, a_class)

"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or
    inherits from, the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
