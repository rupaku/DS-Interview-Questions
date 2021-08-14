'''
https://leetcode.com/problems/count-square-submatrices-with-all-ones/
'''
class Solution:
    def countSquares(self, A: List[List[int]]) -> int:
        countSquares = 0
        
        dp = [[0 for i in A[0]] for j in range(len(A))]
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                # Checking if A[i][j]th element can acutally be used to create a square
                # which will only happen if the element is 1 and there are adjacent elements
                if A[i][j] and i > 0 and j > 0:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = A[i][j]
                
                # Add the count to total count
                countSquares += dp[i][j]
        
        return countSquares