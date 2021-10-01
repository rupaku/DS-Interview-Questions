'''
https://leetcode.com/problems/wiggle-sort-ii/submissions/
'''
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tmp = list(nums)
        tmp.sort(reverse = True)

        mid = len(nums) // 2 
        j = 1
        for i in range(mid):
            nums[j] = tmp[i]
            j += 2
        j = 0
        for i in range(mid, len(nums)):
            nums[j] = tmp[i]
            j += 2

   