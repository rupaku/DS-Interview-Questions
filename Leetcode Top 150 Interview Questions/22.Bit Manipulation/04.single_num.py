# https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            a=a^i # xor all ele ,x ^ 0 return that bit

        return a
        