#https://leetcode.com/problems/non-overlapping-intervals/submissions/1357463490/


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) # sort as end time
        ans=0
        k=-inf # most recent end time
        for x,y in intervals:
            if x >= k:
                k=y
            else:
                ans=ans+1
        return ans
        