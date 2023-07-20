#!/usr/bin/python3
"""
File: 1-my_list.py
Desc: This file contains one class; MyList
Author: Obi Ifeanyi
Date Created: 20 July 2023
"""


class MyList(list):
    """
    Represents the MyList class.
    """

    def print_sorted(self):
        """
        Prints the sorted version of the list.
        """
        print(sorted(self))
