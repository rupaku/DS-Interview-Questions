'''https://leetcode.com/problems/first-bad-version/'''
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        while(left < right):
            mid=left+(right-left)//2
            if(isBadVersion(mid)):
                right=mid
            else:
                left=mid+1
        return left