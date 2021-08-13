'''
https://leetcode.com/problems/the-skyline-problem/submissions/
https://www.youtube.com/watch?v=W2afZs9DYYA
'''
from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events=[]
        for l,r,h in buildings:
            events.append((l,-h,0)) #start
            events.append((r,h,1)) # end
        events.sort()
        
        ans=[]
        active_heights=SortedList([0])
        n=len(events)
        i=0
        while i < n:
            x,h,t=events[i]
            if t == 0:
                active_heights.add(-h)
            else:
                active_heights.discard(h)
            i=i+1
            if not ans or ans[-1][1] != active_heights[-1]:
                ans.append((x,active_heights[-1]))
                
        return ans
        