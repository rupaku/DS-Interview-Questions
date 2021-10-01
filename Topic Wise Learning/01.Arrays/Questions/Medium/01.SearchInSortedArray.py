'''
https://leetcode.com/problems/search-in-rotated-sorted-array/
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1
        left=0
        right=len(nums)-1
        while(left < right):
            mid=left+(right-left)//2
            if (nums[mid] > nums[right]):
                left=mid+1
            else:
                right=mid
                
        start=left
        left=0
        right=len(nums)-1
        if (target >= nums[start] and target <= nums[right]):
            left=start
        else:
            right=start
            
        while(left <= right):
            mid=left+(right-left)//2
            if nums[mid] == target:
                return mid
            elif(nums[mid] < target):
                left=mid+1
            else:
                right=mid-1
        return -1