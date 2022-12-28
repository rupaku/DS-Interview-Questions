'''
https://www.codingninjas.com/codestudio/problems/sudoku-solver_699919?leftPanelTab=1
'''
''' 
    Time Complexity - O(9^K)
    Space Complexity - O(1)

    where K is the number of empty cells in the sudoku.
'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

# Function to check whether we can put a particular value
# to a particular position or not.
def canPut(sudoku, row, col, num):

    for i in range(9):

        if(sudoku[i][col] == num or sudoku[row][i] == num):
            return False

        if(sudoku[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num):
            return False

    return True


# Function to check all the valid way to solve the sudoku.
def backTrack(sudoku, i, j):

    if (j == 9):
        if (i == 8):
            return True

        j = 0
        i += 1

    if (sudoku[i][j] != 0):
        return backTrack(sudoku, i, j + 1)

    # Trying all possible values.
    for put in range(1, 10):

        if (canPut(sudoku, i, j, put)):
            sudoku[i][j] = put
            if (backTrack(sudoku, i, j + 1)):
                return True

            sudoku[i][j] = 0

    return False


def solveSudoku(sudoku):
    backTrack(sudoku, 0, 0)

