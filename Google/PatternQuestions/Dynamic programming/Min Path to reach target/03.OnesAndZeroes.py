'''https://leetcode.com/problems/ones-and-zeroes/submissions/965688865/'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0 for i in range(m+1)] for i in range(n+1)]
        for s in strs:
            ones=s.count("1")
            zeroes=s.count("0")
            for i in range(n,ones-1,-1):
                for j in range(m,zeroes-1,-1):
                    dp[i][j]=max(dp[i][j], dp[i-ones][j-zeroes]+1)
        return dp[n][m]