'''
https://www.codingninjas.com/codestudio/problems/n-queens_759332
'''

'''
    Time Complexity : O(N!)
    Space Complexity : O(N)
    
    Where N is the number of queens.
'''

def addSolution(n, ans, row):
    currentAnswer = []
    for i in range(n):
        for j in range(n):
            if row[j] == i:
                currentAnswer.append(1)
            else:
                currentAnswer.append(0)
    ans.append(currentAnswer)

def solve(col, n, ans, row, d1, d2):
    if col == n:
        addSolution(n, ans, row)
        return
    for i in range(n):
        if ((row[i] == -1) and (d1[col - i + n - 1] == -1) and (d2[col + i] == -1)):
            row[i] = d1[col - i + n - 1] = d2[col + i] = col
            solve(col + 1, n, ans, row, d1, d2)
            row[i] = d1[col - i + n - 1] = d2[col + i] = -1
    return

def solveNQueens(n):
    ans = []
    row = [-1] * 30
    d1 = [-1] * 30
    d2 = [-1] * 30
    solve(0, n, ans, row, d1, d2)
    return ans
