'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

two pointers low first index high as last index check sum with target
if equal = return low+1, high+1 index
if num < target -> low++
else -> high --
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0
        high=len(numbers)-1
        while low < high:
            num= numbers[low]+numbers[high]
            if num == target:
                return (low+1,high+1)
            elif num < target:
                low=low+1
            else:
                high=high-1
        return [-1,-1]
        