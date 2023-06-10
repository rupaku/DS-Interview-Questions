'''https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/964298642/'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_0=0
        longest_win=0
        start=0
        for i in range(len(nums)):
            count_0=count_0+ (nums[i] == 0)
            while count_0 > 1:
                count_0=count_0 - (nums[start] == 0)
                start=start+1
            longest_win= max(longest_win,i-start)
        return longest_win