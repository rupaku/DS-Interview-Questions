'''
https://leetcode.com/problems/find-pivot-index/
comapre left sum with totalsum-left_sum-current ele else leftsum+curre ele
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S=sum(nums)
        left_sum=0
        for i,x in enumerate(nums):
            if left_sum == (S-left_sum-x):
                return i
            left_sum += x
            
        return -1
        