'''
https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/3080/

merge two arrays in sorted order, find mid.
if len(array) % 2 == 0 i.e even -> array[m]+arr[m+1]//2 else array[m]
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_array = nums1+nums2
        merge_array.sort()
        midpoint = math.ceil(len(merge_array)/2.0)-1
        if len(merge_array) % 2 == 0:
            median = (merge_array[midpoint] + merge_array[midpoint+1])/2.0 
        else:
            median= merge_array[midpoint]
        return median
        