'''
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/
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
        