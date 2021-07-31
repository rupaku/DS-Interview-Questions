'''
https://leetcode.com/problems/maximum-product-subarray/submissions/

start with index 0 as max_so_far and max_so_far

find max(curr, max_so_far*curr, min_so_far*curr)
min(curr, max_so_far*curr, min_so_far*curr)

return max(max_so_far,res)
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_so_far = nums[0] # to handle positive num
        min_so_far = nums[0] # to handle negative num
        res = max_so_far
        
        for i in range(1,len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far*curr, min_so_far*curr)
            min_so_far = min(curr, max_so_far*curr, min_so_far*curr)
            
            max_so_far = temp_max
            res= max(max_so_far, res)
            
        return res
        