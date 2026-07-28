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
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# defining a function that not only takes input from the user but converts from a string to integers
def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}: ").split()
        row = [int(val) for val in row_input]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(f"{val:4d}", end="")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    return transposed


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for r in range(rows):
        row_sum = []
        for c in range(cols):
            row_sum.append(matrix_a[r][c] + matrix_b[r][c])
        result.append(row_sum)
    return result


def multiply_matrices(matrix_a, matrix_b):
    # matrix_a is MxN, matrix_b is NxP, cols of a have to match rows of b
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []
    for i in range(rows_a):
        row_result = []
        for j in range(cols_b):
            cell_sum = 0
            for k in range(cols_a):
                cell_sum += matrix_a[i][k] * matrix_b[k][j]
            row_result.append(cell_sum)
        result.append(row_result)

    return result


def main():
    print("Transpose a Matrix")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    print(f"Enter Matrix A ({m}x{n}):")
    matrix_a = read_matrix(m, n)

    print("\nOriginal Matrix A:")
    print_matrix(matrix_a)

    transposed_a = transpose_matrix(matrix_a)
    print("\nTransposed Matrix A:")
    print_matrix(transposed_a)

    print("\n" + "-" * 30)

    print("Add Two Matrices")
    print(f"Enter second matrix (Matrix B) of same size ({m}x{n}):")
    matrix_b = read_matrix(m, n)

    sum_result = add_matrices(matrix_a, matrix_b)
    print("\nMatrix Addition (A + B):")
    print_matrix(sum_result)

    print("\n" + "-" * 30)

    print("Multiply Two Matrices")
    p = int(input(f"Enter number of columns for Matrix C (Rows fixed at {n}): "))

    print(f"Enter Matrix C of size {n}x{p}:")
    matrix_c = read_matrix(n, p)

    product_result = multiply_matrices(matrix_a, matrix_c)
    print("\nMatrix Multiplication (A x C):")
    print_matrix(product_result)


if __name__ == "__main__":
    main()