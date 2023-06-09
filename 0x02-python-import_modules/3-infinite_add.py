#!/usr/bin/python3
import sys


def sum_args(args):
    total = sum(int(arg) for arg in args[1:])
    return "{}".format(total)


if __name__ == "__main__":
    print(sum_args(sys.argv))
