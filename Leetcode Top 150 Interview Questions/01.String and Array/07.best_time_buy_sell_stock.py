#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150


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

        