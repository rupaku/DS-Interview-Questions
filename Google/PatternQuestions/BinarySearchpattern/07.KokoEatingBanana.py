'''https://leetcode.com/problems/koko-eating-bananas/submissions/960154518/'''
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def feasible(speed):
            return sum((pile - 1) // speed + 1 for pile in piles) <= H  # faster
        l=1
        r=max(piles)
        while l < r:
            m = (l + r) // 2
            if feasible(m):
                r = m
            else:
                l = m + 1
        return l