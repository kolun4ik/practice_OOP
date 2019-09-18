# Test 9x9 matrix filled with numbers from 1 to 9
# in accordance with sudoku rules
# The cells of the sudoku board may also contain 0's,
# which will represent empty cells

from collections import Counter


def validSolution(matrix):
    """Sudoku Solution Validator"""
    rows = cells = blocks = True

    if len(matrix) == 9 and len(matrix[0]):

        for j in range(9):
            cell = []

            for key, val in Counter(matrix[j]).items():
                if val != 1:
                    rows = False

            for i in range(9):
                 cell.append(matrix[i][j])

            for k, v in Counter(cell).items():
                if v != 1:
                    cells = False
        # for block: shred dataset on blocks 3x3

        return rows and cells and blocks
    else:
        raise ValueError("Матрица не соответствует размерности 9 Х 9".format(matrix))