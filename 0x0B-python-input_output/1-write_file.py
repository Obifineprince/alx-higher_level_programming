#!/usr/bin/python3
"""
Description: This module has one function;
write_file(filename="", text="")
"""

def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
