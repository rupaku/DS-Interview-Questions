'''
https://leetcode.com/problems/single-element-in-a-sorted-array/
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while(l < h):
            mid=l+(h-l)//2
            if mid % 2 == 1:
                mid=mid-1
            #we want only even index
            if nums[mid] == nums[mid+1]:
                l=mid+2
            else:
                h=mid
        return nums[l]
        