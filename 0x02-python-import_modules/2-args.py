#!/usr/bin/python3
import sys


def print_arguments(args):
    num_args = len(args) - 1
    print(f"{num_args} argument{'s' if num_args != 1 else ''}:")
    for i, arg in enumerate(args[1:], start=1):
        print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments(sys.argv)
