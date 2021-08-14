'''
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/submissions/
'''
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        res1=nums[-4]-nums[0]
        res2=nums[-3]-nums[1]
        res3=nums[-2]-nums[2]
        res4=nums[-1]-nums[3]
        return min(res1,res2,res3,res4)
        