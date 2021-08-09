'''
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
'''
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        index=nums.index(max(nums))
        nums.sort()
        maximum=nums[-1]
        nums.pop(-1)
        if len(nums)==0:
            return 0
        if nums[-1]*2<=maximum:
            return index
        else:
            return -1