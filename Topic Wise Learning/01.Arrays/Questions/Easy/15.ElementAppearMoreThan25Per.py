'''
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/submissions/
'''
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dict1 = collections.Counter(arr)
        for each in dict1:
            if dict1[each] > float(len(arr))/4:
                return each