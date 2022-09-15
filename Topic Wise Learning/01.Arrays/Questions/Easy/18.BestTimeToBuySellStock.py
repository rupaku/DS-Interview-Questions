'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ '''


class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if prices == []:
#             return 0
#         buy = prices[0]
#         max_profit=0
        
#         for i in range(1,len(prices)):
#             profit = prices[i] - buy
            
#             if profit > max_profit:
#                 max_profit=profit
                
#             if buy > prices[i]:
#                 buy = prices[i]
                
#         return max_profit
        # def maxProfit(self, prices: List[int]) -> int:
        #     min_price = float('inf')
        #     max_profit =0
        #     for i in range(len(prices)):
        #         if prices[i] < min_price:
        #             min_price = prices[i]
        #         elif prices[i] - min_price > max_profit:
        #             max_profit = prices[i] - min_price
        #     return max_profit
        
            def maxProfit(self,prices:List[int]) -> int:
                l=0
                r=1
                maxP=0
                while (r <len(prices)):
                    if prices[l] < prices[r]:
                        profit = prices[r] - prices[l]
                        maxP=max(maxP,profit)
                    else:
                        l=r
                    r=r+1
                return maxP