'''https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/'''
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        start=-1
        end=-1
        res=0
        for i in range(len(nums)):
            if nums[i] > right:
                start=i
                end=i
                continue
            if nums[i] >= left:
                end=i
            res=res+end-start
        return res