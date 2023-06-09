#!/usr/bin/python3
from calculator_1 import sub, add, div, mul
import sys


def calculate(a, op, b):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mul(a, b)
    elif op == "/":
        return div(a, b)
    else:
        raise ValueError(f"Unknown operator: {op}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    try:
        result = calculate(a, op, b)
        print(f"{a} {op} {b} = {result}")
    except ValueError as e:
        print(e)
        sys.exit(1)
