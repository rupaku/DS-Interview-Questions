'''
https://leetcode.com/problems/search-a-2d-matrix-ii/submissions/
'''
class Solution:
    def binary_search(self,matrix,target,start,vertical):
        l=start
        h=len(matrix[0])-1 if vertical else len(matrix)-1
        
        while l <= h:
            mid=(l+h)//2
            if vertical:
                if matrix[start][mid] < target:
                    l=mid+1
                elif matrix[start][mid] > target:
                    h=mid-1
                else:
                    return True
            else:
                if matrix[mid][start] < target:
                    l=mid+1
                elif matrix[mid][start] > target:
                    h=mid-1
                else:
                    return True
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        #iterate diagonals
        for i in range(min(len(matrix),len(matrix[0]))):
            vertical_found=self.binary_search(matrix,target,i,True)
            horizontal_found=self.binary_search(matrix,target,i,False)
            if vertical_found or horizontal_found:
                return True
            
        return False
        