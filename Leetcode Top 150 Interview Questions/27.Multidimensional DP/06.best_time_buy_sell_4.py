# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k== 0:
            return 0

        dp_cost = [float("inf")]*k
        dp_profit = [0]*k

        for price in prices:
            for i in range(k):
                # the maximum profit if only one transaction is allowed
                if i == 0:
                    dp_cost[i] = min(dp_cost[i], price)
                    dp_profit[i] = max(dp_profit[i], price - dp_cost[i])
                else:
                    # reinvest the gained profit in the second transaction
                    dp_cost[i] = min(dp_cost[i], price - dp_profit[i-1])
                    dp_profit[i] = max(dp_profit[i], price - dp_cost[i])

        return dp_profit[-1]