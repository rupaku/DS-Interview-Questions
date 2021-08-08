'''
https://leetcode.com/problems/minimum-size-subarray-sum/submissions/
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        ans = float('inf')
        total = 0
        for l in range(len(nums)):
            while r < len(nums) and total < target:
                total=total+nums[r]
                r=r+1
            if total >= target:
                ans=min(ans,r-l)
            total = total - nums[l]
        if ans == float('inf'):
            return 0
        else:
            return ans
        