'''
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        i=0
        j=1
        s=0
        while j <= len(nums)-1:
            s=s+min(nums[i],nums[j])
            i=i+2
            j=j+2
        return s
        