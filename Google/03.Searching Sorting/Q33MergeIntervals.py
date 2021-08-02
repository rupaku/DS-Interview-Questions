'''
https://leetcode.com/problems/merge-intervals/submissions/
https://www.youtube.com/watch?v=iT9_MU2L3H0
sort intervals
output list with 0th index
check start > prev end of output -> insert in output
else: prev end output = end of current interval
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        output =[intervals[0]]
        for start,end in intervals[1:]:
            #start > prev interval end
            if start > output[-1][1]:
                #insert
                output.append([start,end])
            elif end > output[-1][1]:
                #update
                output[-1][1] = end
        return output