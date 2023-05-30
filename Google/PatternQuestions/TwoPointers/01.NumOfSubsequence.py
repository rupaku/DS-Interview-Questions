'''https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/'''
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        low=0
        high=len(nums)-1
        cnt=0
        while low <= high:
            num=nums[low]+nums[high]
            if num <= target:
                ans=ans+2**(high-low)
                ans=ans%(10**9+7)
                low=low+1
            elif num > target:
                high=high-1
        return ans%(10**9+7)  
