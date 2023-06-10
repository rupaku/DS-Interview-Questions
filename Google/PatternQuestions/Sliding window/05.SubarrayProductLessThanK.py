''''''
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = i = 0
        for j, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[i]
                i += 1
            ans += j - i + 1
        return ans