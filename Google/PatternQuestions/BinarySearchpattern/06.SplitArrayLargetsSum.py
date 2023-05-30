'''https://leetcode.com/problems/split-array-largest-sum/submissions/960148316/'''
class Solution(object):
    def splitArray(self, nums, m):
        def is_possible(threshold):
            total=0
            cnt=1
            for num in nums:
                total=total+num
                if total > threshold:
                    total=num
                    cnt=cnt+1
                    if cnt > m:
                        return False
            return True

        l = max(nums)
        r = sum(nums)
        while l < r:
            mid = l + (r-l)//2
            if is_possible(mid):
                r = mid
            else:
                l = mid+1
        return l