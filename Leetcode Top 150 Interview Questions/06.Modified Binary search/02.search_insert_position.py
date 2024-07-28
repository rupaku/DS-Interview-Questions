#https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l <= r:
            mid=l+(r-l)//2
            if nums[mid] < target:
                l=mid+1
            elif nums[mid] > target:
                r=mid -1
            elif nums[mid] ==  target:
                return mid
        return l