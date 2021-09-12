'''
https://leetcode.com/problems/sort-array-by-increasing-frequency/submissions/
'''
import collections
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        #reverse the array
        nums.sort(reverse=True)
        
        #Sort them according to their counts
        ans = sorted(nums, key = nums.count)
        
        return ans