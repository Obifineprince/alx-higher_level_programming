#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    def is_safe(board, row, col):
        """Check if it's safe to place a queen at board[row][col]"""
        for i in range(col):
            if board[i] == row or \
               board[i] == row - (col - i) or \
               board[i] == row + (col - i):
                return False
        return True

    def solve_nqueens(board, col, solution):
        """Solve the N queens problem using backtracking"""
        if col >= n:
            # All queens are placed, print the solution
            formatted_solution = str(solution).replace(", ", ",")
            formatted_solution = formatted_solution.replace("[[", "[")
            formatted_solution = formatted_solution.replace("]]", "]")
            print(formatted_solution)
            return

        for row in range(n):
            if is_safe(board, row, col):
                # Place the queen at board[row][col]
                board[col] = row

                # Recur to place the rest of the queens
                solve_nqueens(board, col + 1, solution + [[row, col]])

    # Create an empty board
    board = [-1] * n

    # Solve the N queens problem
    solve_nqueens(board, 0, [])
