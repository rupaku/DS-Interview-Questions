'''
https://leetcode.com/problems/search-a-2d-matrix-ii/
'''
class Solution:
    def searchMatrixII(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        row_index=0
        col_index=col-1
        while row_index < row and col_index >= 0:
            ele=matrix[row_index][col_index]
            if ele == target:
                return 1
            if ele < target:
                row_index=row_index+1
            else:
                col_index=col_index-1
        return 0
        