'''https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/958841638/'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
#         for i in range(len(nums)-1,0,-1):
#             if nums[i-1] == nums[i]:
#                 nums.pop(i)

#         return len(nums)
      if len(nums) == 0:
         return 0
      i=0
      for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i=i+1
                nums[i] =nums[j]
      return i +1
            
            
                