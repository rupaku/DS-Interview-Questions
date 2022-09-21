'''
Pivot element (min in graph)
'''
class Solution:
    def pivot_element(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while l <= h:
            mid=(l+h)//2
            if nums[mid] >= nums[0]:
                l=mid+1
            else:
                h=mid
        return l
        