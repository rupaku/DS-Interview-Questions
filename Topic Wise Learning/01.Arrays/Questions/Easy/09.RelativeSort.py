'''
https://leetcode.com/problems/relative-sort-array/submissions/
'''
import collections
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        h = collections.Counter(arr1)
        result = []
        for num in arr2:
            result += [num] * h.get(num)
            del h[num]
        arr = sorted(h.keys())
        for num in arr:
            result += [num] * h.get(num)
        return result        