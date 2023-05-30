'''https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/submissions/958519219/'''
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        low=0
        high=len(nums)-1
        res=0
        while low <= high:
            res=max(res,nums[low]+nums[high])
            low=low+1
            high=high-1
        return res