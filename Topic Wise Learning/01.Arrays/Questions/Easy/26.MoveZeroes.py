'''
https://leetcode.com/problems/move-zeroes/submissions/

time  O(n)
space O(1)
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        count=0
        for i in range(n):
            if nums[i]!=0:
                nums[count]=nums[i]
                count=count+1
        while count < n:
            nums[count]=0
            count=count+1
        


