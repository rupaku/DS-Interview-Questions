'''
https://leetcode.com/problems/running-sum-of-1d-array/submissions/
'''
class Solution:
    # def runningSum(self, nums: List[int]) -> List[int]:
    #     sm=0
    #     res=[]
    #     for i in nums:
    #         sm=sm+i
    #         res.append(sm)
    #     return res
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums