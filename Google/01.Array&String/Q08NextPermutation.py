'''
https://leetcode.com/problems/next-permutation/
https://www.youtube.com/watch?v=6qXO72FkqwM
swap least weightage peak with nearest to left, then sort digits after right of swap
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k =len(nums) -2 #2nd last ele
        l=len(nums) - 1 #last ele
        while k >= 0 and nums[k] >= nums[k+1]: 
            k -= 1 
        if k == -1: 
            return nums.reverse() 
        while nums[k] >= nums[l]:  
            l -= 1  
        nums[k], nums[l] = nums[l], nums[k]  
        nums[k+1:]=reversed(nums[k+1:]) 
        