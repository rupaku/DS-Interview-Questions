# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        c=0
        for i in nums:
            if c < 2 or i != nums[c-2]:
                nums[c] = i
                c=c+1
        return c
