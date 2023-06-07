#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return (str)
    for j in range(0, len(str)):
        if j == n:
            new_str = str[:j] + str[j+1] + str[j+2:]
            return (new_str)
