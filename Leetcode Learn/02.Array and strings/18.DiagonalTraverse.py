'''
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
https://www.youtube.com/watch?v=0DnG0Kc9M2E
'''
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return
        num_rows=len(mat)
        num_cols=len(mat[0])
        diagonal=[[] for _ in range(num_rows+num_cols-1)]
        
        for i in range(num_rows):
            for j in range(num_cols):
                diagonal[i+j].append(mat[i][j])
                
        res=diagonal[0]
        for x in range(1,len(diagonal)):
            if x%2==1:
                res.extend(diagonal[x])
            else:
                res.extend(diagonal[x][::-1])
        return res
                
            
        