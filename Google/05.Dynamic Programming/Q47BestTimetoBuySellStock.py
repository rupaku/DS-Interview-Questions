'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/
We can maintain two variables 
- minprice and maxprofit corresponding to the smallest valley
 and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.


'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        buy = prices[0]
        max_profit=0
        
        for i in range(1,len(prices)):
            profit = prices[i] - buy
            
            if profit > max_profit:
                max_profit=profit
                 
            if buy > prices[i]:
                buy = prices[i]
                
        return max_profit
        