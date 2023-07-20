#!/usr/bin/python3
"""
File: 0-lookup.py
Description: This module contains a function called 'lookup' that returns the list
of attributes and methods available for a given object.
Author: Obi Ifeanyi
Date Created: July 20, 2023
"""
def lookup(obj):
    """
    Retrieves a list of attributes and methods available for the specified object.
    """
    return dir(obj)
