'''https://leetcode.com/problems/find-k-th-smallest-pair-distance/submissions/960440385/'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def enough(distance) -> bool:  # two pointers
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:  # move fast pointer
                    j += 1
                count += j - i - 1  # count pairs
                i += 1  # move slow pointer
            return count >= k
        nums.sort()
        n = len(nums)
        l=0
        r=nums[-1]-nums[0]
        while l < r:
            m=l+(r-l)//2
            if enough(m):
                r=m
            else:
                l=m+1
        return l