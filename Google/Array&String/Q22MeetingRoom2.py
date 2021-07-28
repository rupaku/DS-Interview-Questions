'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3059/
https://www.youtube.com/watch?v=FdzJmTCVyJU

sorted array of start and end
compare all start index with end1 index, if s < e, c++
if s== e , e++
if all start index ends ,loop ends
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=sorted([i[0] for i in intervals])
        end=sorted([i[1] for i in intervals])
        res=0
        count=0
        s=0
        e=0
        while s < len(intervals):
            if start[s] < end[e]:
                s=s+1
                count = count+1
            else:
                e = e+1
                count=count -1
            res= max(res,count)
        return res