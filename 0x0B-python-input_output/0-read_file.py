#!/usr/bin/python3
"""
Desc: This module has one function; read_file(filename="")
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end='')
