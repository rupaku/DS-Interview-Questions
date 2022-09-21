'''https://leetcode.com/problems/sqrtx/submissions/
O(logn)
O(1)
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l=2
        h=x//2
        while l <= h:
            pivot=l+(h-l)//2
            num=pivot*pivot
            if x > num:
                l=pivot+1
            elif x < num:
                h=pivot-1
            else:
                return pivot
        return h
        