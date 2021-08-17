'''
https://leetcode.com/problems/koko-eating-bananas/submissions/
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        import math
        l, r = 1, int(math.pow(10,9))
        while l < r:
            m = (l + r) // 2
            cnt = sum([math.ceil(p/m) for p in piles])
            if cnt > H:
                l = m + 1
            else:
                r = m
        return l