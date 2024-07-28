#https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=sorted([i[0] for i in intervals])
        end=sorted([i[1] for i in intervals])
        s=0
        e=0
        res=0
        count=0
        while s < len(intervals):
            if start[s] < end[e]:
                s=s+1
                count=count+1
            else:
                e=e+1
                count=count-1
            res=max(res,count)
        return res