#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()
        # Get the first two elements from each tuple, or use 0 if a tuple has fewer than 2 element
        a1, a2 = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
        b1, b2 = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)

        # Add the corresponding elements of the tuples
        result = (a1 + b1, a2 + b2)


        return result

