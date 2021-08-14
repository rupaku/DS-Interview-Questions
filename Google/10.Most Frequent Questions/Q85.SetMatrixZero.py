'''
https://leetcode.com/problems/set-matrix-zeroes/submissions/
we can use the first cell of every row and column as a flag.
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        r=len(matrix)
        c=len(matrix[0])
        is_col=False
        for i in range(r):
            if matrix[i][0] == 0:
                is_col=True
            for j in range(1,c):
                if matrix[i][j] == 0:
                    matrix[0][j] =0
                    matrix[i][0] =0
                    
        
        #update array according to flag
        for i in range(1,r):
            for j in range(1,c):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j]=0
         
        #if first row needs to be set to zero
        if matrix[0][0] == 0:
            for j in range(c):
                matrix[0][j] =0
              
        #if first col needs to be set to zero
        if is_col:
            for i in range(r):
                matrix[i][0]=0
            