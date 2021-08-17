'''
https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/submissions/
https://www.youtube.com/watch?v=eWweg7QwB6A
'''
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        m=len(mat)
        n=len(mat[0])
        dp=[[(0,0,0,0)]*(n+2) for _ in range(m+1)]
        ans=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if mat[i-1][j-1] == 1:
                    # 4 directions-> horizonatal.vertical.diagonal,anti diagonal
                    dp[i][j]=(dp[i][j-1][0]+1,dp[i-1][j-1][1]+1,dp[i-1][j][2]+1,dp[i-1][j+1][3]+1)
                    ans=max(ans,max(dp[i][j]))
        
        return ans