
'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/submissions/
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        start = matrix[0][0]
        end=matrix[n-1][n-1]
        
        while start < end:
            mid = start + (end-start)/2
            smaller,larger = (matrix[0][0],matrix[n-1][n-1])
            
            count,smaller,larger= self.countLessEqual(matrix,mid,smaller,larger)
            
            if count == k:
                return smaller
            if count < k:
                start = larger
            else:
                end=smaller
        return start
    
    def countLessEqual(self, matrix, mid, smaller, larger):
        count=0
        n=len(matrix)
        row=n-1
        col=0
        
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                larger= min(larger,matrix[row][col])
                row=row-1
            else:
                smaller=max(smaller,matrix[row][col])
                count=count+row+1
                col=col+1
        return count,smaller,larger
        