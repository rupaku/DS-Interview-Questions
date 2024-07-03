# https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150

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
                if target == num:
                    res.add(nums[0],nums[low],nums[high])
                    low=low+1
                    high=high-1
                elif target < num:
                    low=low+1
                else:
                    high=high-1
        return list(res)
    
    