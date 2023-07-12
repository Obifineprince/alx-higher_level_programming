#!/usr/bin/python3
"""
File: 101-locked_class.py
Desc: This module defines the LockedClass, which restricts the dynamic creation
of new instance attributes, except for the first_name attribute.
Author: Obi Ifeanyi Princewill
Date Created: 5 July 2023
"""


class LockedClass:
    """
    This class restricts the user from dynamically creating new instance attributes,
    except for the first_name attribute.
    """
    __slots__ = ["first_name"]
