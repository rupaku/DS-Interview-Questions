'''
https://leetcode.com/problems/3sum/
low=i+1
high =last ele
current sum = nums[i]+nums[low]+nums[high]
if CS < 0 : low++
elif CS > 0: high --
else append in list low++,high --
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum2(nums, i, res)
        return res
                
    def twoSum2(self,nums: List[int], i:int, res:List[List[int]]):
        low=i+1
        high =len(nums)-1
        while(low < high):
            current_sum = nums[i] +nums[low]+nums[high]
            if current_sum < 0:
                low=low+1
            elif current_sum > 0:
                high=high-1
            else:
                res.append([nums[i],nums[low],nums[high]])
                low=low+1
                high=high-1
                while low < high and nums[low] == nums[low-1]:
                    low=low+1
        
        