#!/usr/bin/python3

"""
Desc: This module has one function;
append_write(filename="", text="")
"""

def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
