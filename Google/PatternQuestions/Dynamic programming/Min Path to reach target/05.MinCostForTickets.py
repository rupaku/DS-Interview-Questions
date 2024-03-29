''''''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset=set(days)
        durations=[1,7,30]

        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i+d) + c for c,d in zip(costs,durations))
            else:
                return dp(i+1)
        return dp(1)