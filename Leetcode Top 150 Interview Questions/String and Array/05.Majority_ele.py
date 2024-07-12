#https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def majority(nums):
        cand=None
        count=0
        for num in nums:
            if count == 0:
                cand=num
            count+=(1 if num == cand else -1)
        return cand
