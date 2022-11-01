'''
https://leetcode.com/problems/subsets/submissions/
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # init res
        res = []

        # call helper function
        self.helper(nums, [], res)

        # return res
        return res

    def helper(self, nums, tmp, res):
        # base cases
        res.append(tmp)

        # recursion
        for i in range(len(nums)):
            self.helper(nums[i+1:], tmp + [nums[i]], res)