# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))

       
        while len(row) != cols:
            print("Error: Enter exactly", cols, "numbers.")
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))

        matrix.append(row)

    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end="\t")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []

        for i in range(rows):
            new_row.append(matrix[i][j])

        transpose.append(new_row)

    return transpose


def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])

    result = []

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(A[i][j] + B[i][j])

        result.append(row)

    return result


# PART C: Multiply Two Matrices
def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = []

    for i in range(rows_A):
        row = []

        for j in range(cols_B):
            total = 0

            for k in range(cols_A):
                total = total + A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result


# ---------------- MAIN PROGRAM ----------------


print("PART A: Matrix Transpose")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nTransposed Matrix:")
display_matrix(transpose_matrix(matrix))


print("\nPART B: Matrix Addition")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter Matrix A:")
A = read_matrix(rows, cols)

print("Enter Matrix B:")
B = read_matrix(rows, cols)

print("\nMatrix A + Matrix B:")
display_matrix(add_matrices(A, B))


print("\nPART C: Matrix Multiplication")

rows_A = int(input("Enter rows of Matrix A: "))
cols_A = int(input("Enter columns of Matrix A: "))

rows_B = int(input("Enter rows of Matrix B: "))
cols_B = int(input("Enter columns of Matrix B: "))


if cols_A != rows_B:
    print("Error: Columns of A must equal rows of B.")
else:
    print("Enter Matrix A:")
    A = read_matrix(rows_A, cols_A)

    print("Enter Matrix B:")
    B = read_matrix(rows_B, cols_B)

    print("\nMatrix A x Matrix B:")
    display_matrix(multiply_matrices(A, B))