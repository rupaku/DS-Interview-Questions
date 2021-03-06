'''
https://leetcode.com/problems/maximum-subarray/solution/
find current max with max(nums[i], curr_max+nums[i])
then max_so far with max(curr_max,max_so_far)

return max_so_far
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:     
        max_so_far =nums[0] 
        curr_max = nums[0] 
        size=len(nums) 
        for i in range(1,size): 
            curr_max = max(nums[i], curr_max + nums[i]) 
            max_so_far = max(max_so_far,curr_max) 
          
        return max_so_far 
   
        