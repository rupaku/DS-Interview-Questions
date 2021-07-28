'''
https://leetcode.com/problems/peak-index-in-a-mountain-array/solution/
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        h=len(arr)-1
        while l < h:
            m=(l+h)//2
            if arr[m] < arr[m+1]:
                l=m+1
            else:
                h=m
        return l
                