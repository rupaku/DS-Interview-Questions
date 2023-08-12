'''https://leetcode.com/problems/3sum/'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)):
            low=i+1
            high=len(nums)-1
            target=0-nums[i]
            while low < high:
                num=nums[low]+nums[high]
                if num == target:
                    res.add((nums[i],nums[low],nums[high]))
                    low=low+1
                    high=high-1
                elif num < target:
                    low=low+1
                else:
                    high=high-1
        return list(res)