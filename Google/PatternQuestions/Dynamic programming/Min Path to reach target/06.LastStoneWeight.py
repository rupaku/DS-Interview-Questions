'''https://leetcode.com/problems/last-stone-weight-ii/submissions/965790991/'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s={0}
        for st in stones:
            tmp=set()
            for i in s:
                tmp.add(abs(i+st))
                tmp.add(abs(i-st))
            s=tmp
        return min(s) if len(s) > 0 else 0