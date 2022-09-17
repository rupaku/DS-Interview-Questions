'''
https://leetcode.com/problems/intersection-of-two-arrays/solution/
time  O(n+m)
space O(n+m)
'''
class Solution:
    def set_intersect(self,set1,set2):
        return [x for x in set1 if x in set2]
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        set2=set(nums2)
        if len(set1) < len(set2):
            return self.set_intersect(set1,set2)
        else:
            return self.set_intersect(set2,set1)