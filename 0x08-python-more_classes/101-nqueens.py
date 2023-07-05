import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    """
    Solve the N queens problem using backtracking
    """
    if col >= N:
        # All queens are placed, print the solution
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen at board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, col + 1)

            # Backtrack and remove the queen from board[i][col]
            board[i][col] = 0


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty board
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N queens problem
    solve_nqueens(board, 0)
