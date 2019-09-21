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

        # for block: break dataset on blocks 3x3
        tmp = [matrix[i][j] for i in range(9) for j in range(9)]
        data = [
            tmp[:27],
            tmp[27:54],
            tmp[54:]
        ]

        for i in range(3):
            for k, v in Counter(
                    data[i][:3] + data[i][9:12] + data[i][18:21]).items():
                if v != 1:
                    blocks = False

            for k, v in Counter(
                    data[i][3:6] + data[i][12:15] + data[i][21:24]).items():
                if v != 1:
                    blocks = False

            for k, v in Counter(
                    data[i][6:9] + data[i][15:18] + data[i][24:]).items():
                if v != 1:
                    blocks = False

        return rows and cells and blocks
    else:
        raise ValueError(
            "Матрица не соответствует размерности 9 Х 9".format(matrix)
        )


def blockBreaker(matrix):
    """Divides the square matrix into blocks:
     testing the algorithm for breaking into blocks for the subsequent
     validating them according to sudoku rules."""

    tmp = [matrix[i][j] for i in range(9) for j in range(9)]
    data = [
        tmp[:27],
        tmp[27:54],
        tmp[54:]
    ]

    for i in range(3):
        print(data[i][:3] + data[i][9:12] + data[i][18:21])
        print(data[i][3:6] + data[i][12:15] + data[i][21:24])
        print(data[i][6:9] + data[i][15:18] + data[i][24:])
