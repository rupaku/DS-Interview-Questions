'''
https://leetcode.com/problems/container-with-most-water/
l with all each time , distance between l and r and least height

whichever will be smaller among l and r , will shift and find area of max and update accordingly
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ans=0
    
        while(l <r):
            ans=max(ans,min(height[l],height[r])* (r-l)) # h *l area height minimum is considered
            
            if height[l] < height[r]:
                l=l+1
            else:
                r=r-1
        return ans
            
        