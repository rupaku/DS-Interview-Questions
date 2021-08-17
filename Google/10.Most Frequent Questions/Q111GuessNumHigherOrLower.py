'''
https://leetcode.com/problems/guess-number-higher-or-lower-ii/submissions/
https://www.youtube.com/watch?v=DMsjVzboYnI
'''
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        cost=[[0]*(n+1) for _ in range(n+1)]
        for low in range(n,0,-1):
            for high in range(low+1,n+1):
                cost[low][high]=min(i+max(cost[low][i-1],cost[i+1][high]) for i in range(low,high))
                
        return cost[1][n]
        