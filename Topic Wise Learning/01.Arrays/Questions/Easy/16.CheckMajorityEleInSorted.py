'''
https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/submissions/
'''
class Solution:        
    def isMajorityElement(self, nums, target):
        def search(a, x):
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        N = len(nums)
        if nums[N // 2] != target:
            return False
        lo = search(nums, target)
        hi = search(nums, target + 1)
        return hi - lo > N // 2