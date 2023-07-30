'''https://leetcode.com/problems/unique-binary-search-trees/submissions/965932518/?envType=list&envId=55aj8s16'''
class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1 #with empty tree
        dp[1]=1 #with only root
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
        