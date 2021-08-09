'''
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1151/
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val):
            nums.remove(val)
        