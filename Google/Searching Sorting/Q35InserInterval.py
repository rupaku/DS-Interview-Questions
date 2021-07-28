'''
https://leetcode.com/problems/insert-interval/

output[-1][1] -> previous end

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        index=0
        n=len(intervals)
        output=[]
        #add all intervals starting before newInerval
        while index < n and new_start > intervals[index][0]:
            output.append(intervals[index])
            index=index+1
            
        #add new interval (if no overlap)
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        else:
            #if overlap, merge with last interval
            output[-1][1]= max(output[-1][1], new_end)
            
        #add next intervals, merge with newIntervals if needed
        while index < n:
            interval =intervals[index]
            start,end=interval
            index=index+1
            #if no overlap, add an interval
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1],end)
        return output
            
        