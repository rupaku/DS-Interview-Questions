# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        
    def transpose(self, matrix):
        n= len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i],matrix[i][j] =matrix[i][j],matrix[j][i]
                
    def reflect(self,matrix):
        n= len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][-j-1] =matrix[i][-j-1],matrix[i][j]
        