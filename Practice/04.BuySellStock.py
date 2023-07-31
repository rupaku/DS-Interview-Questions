'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock/'''

# Solution 1 Iterative [o(n^2), o(1))]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pr =0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                profit=prices[j] -prices[i]
                if profit > max_pr:
                    max_pr=profit
        return max_pr
        
# Solution 2 one pass [o(n), o(1))]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price =float('inf')
        max_pr =0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price=prices[i]
            elif prices[i] - min_price > max_pr:
                max_pr = prices[i] - min_price
        return max_pr

        