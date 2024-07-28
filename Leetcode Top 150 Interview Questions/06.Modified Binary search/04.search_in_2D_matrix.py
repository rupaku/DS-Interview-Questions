#https://leetcode.com/problems/search-a-2d-matrix/editorial/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        start=0
        end=row*col-1
        while start <= end:
            mid=start+(end-start)//2
            ele=matrix[mid//col][mid%col]
            if ele == target:
                return 1
            if ele < target:
                start=mid+1
            else:
                end=mid-1
        return 0
                