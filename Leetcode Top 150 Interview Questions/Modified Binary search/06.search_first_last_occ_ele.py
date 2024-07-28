#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        
        def searchLow(nums, target):
            l, h = 0, len(nums) - 1
            while l <= h:
                mid = (l + h)//2
                if nums[mid] >= target:
                    h = mid - 1
                else:
                    l = mid + 1
            return l
                
        def searchHigh(nums, target):
            l, h = 0, len(nums) - 1
            while l <= h:
                mid = (l + h)//2
                if nums[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1
            return h
        
        start = searchLow(nums, target)
        end = searchHigh(nums, target)
        if 0 <= start < len(nums) and start <= end and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]