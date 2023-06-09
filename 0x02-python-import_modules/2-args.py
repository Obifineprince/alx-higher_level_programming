#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv[1:]
    num_argv = len(argv)
    
    if num_argv == 0:
        print("Number of argument(s): 0.")
        print(".")
    else:
        print("Number of argument(s):", num_argv)
        print("Arguments:", end=" ")
        if num_argv == 1:
            print(argv[0], end="")
        else:
            print(argv, end="")
        print(".")
        
        for i, arg in enumerate(argv):
            print(i+1, ":", arg)
