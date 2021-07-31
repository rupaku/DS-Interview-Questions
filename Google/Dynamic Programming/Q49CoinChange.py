'''
https://leetcode.com/problems/coin-change/solution/
#Bottom up DP
F(3)
​=min{F(3−c1),F(3−c2),F(3−c3)}+1
=min{F(3−1),F(3−2),F(3−3)}+1
=min{F(2),F(1),F(0)}+1
=min{1,1,0}+1
=1
  

'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]* (amount+1)
        dp[0]=0
        
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin] +1)
                
        return dp[amount] if dp[amount]!= float('inf') else -1