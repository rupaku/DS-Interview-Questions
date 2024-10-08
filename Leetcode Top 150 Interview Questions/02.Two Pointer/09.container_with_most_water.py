#https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ans=0
        while l < r:
            ans=max(ans,min(height[l],height[r]) * (r-l))
            if height[l] < height[r]:
                l=l+1
            else:
                r=r-1
        return ans
            
        