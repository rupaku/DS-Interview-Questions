'''
https://leetcode.com/problems/n-queens-ii/submissions/
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row,diagonals,anti_diagonals,cols):
            if row == n:
                return 1
            solutions=0
            for col in range(n):
                curr_diagonal=row-col
                curr_anti_diagonal=row+col
                
                #If queen is not placeable
                if (col in cols or
                    curr_diagonal in diagonals or
                    curr_anti_diagonal in anti_diagonals): 
                    continue
                    
                #Add queen to board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                
                #Move to next row with updated state
                solutions += backtrack(row+1,diagonals,anti_diagonals,cols)
                
                #remove queen from board since already explored all valid paths
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                
            return solutions
        
        return backtrack(0,set(),set(),set())
            
        