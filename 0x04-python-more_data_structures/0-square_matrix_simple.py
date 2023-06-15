#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = matrix
        for num in row:
            square_value = num ** 2
            new_row.append(square_value)
        new_matrix.append(new_row)
    return (new_matrix)
