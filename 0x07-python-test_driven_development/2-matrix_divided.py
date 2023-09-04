def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("Matrix elements must be integers or floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("All rows in the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("Divisor must be a number")

    if div == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    return [[round(num / div, 2) for num in row] for row in matrix]
