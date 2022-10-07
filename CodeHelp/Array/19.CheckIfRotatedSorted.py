'''
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/submissions/
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        # s=sorted(nums)
        # for i in range(len(s)):
        #     if s[i:]+s[:i]==nums:
        #         return True
        # return False
        n=len(nums)
        c=0
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                c=c+1
        if nums[n-1] > nums[0]:
            c=c+1
        return c<=1