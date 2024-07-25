#https://leetcode.com/problems/merge-intervals/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def merge_interval(intervals):
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        output= [intervals[0]]
        for start,end in intervals[1:]:
            if start > output[-1][1]:
                output.append([start,end])
            elif end > output[-1][1]:
                output[-1][1]=end
        return output