#https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l < r:
            mid= l+(r-l)//2
            if nums[mid] > nums[mid+1]:
                r=mid
            else:
                l=mid+1
        return l
        