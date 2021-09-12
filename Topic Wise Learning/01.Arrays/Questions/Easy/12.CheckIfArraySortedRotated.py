'''
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/submissions/
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        s=sorted(nums)
        for i in range(len(s)):
            if s[i:]+s[:i]==nums:
                return True
        return False