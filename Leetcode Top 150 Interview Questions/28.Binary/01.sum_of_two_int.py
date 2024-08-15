# https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        x=abs(a)
        y=abs(b)

        if x < y:
            return self.getSum(b,a)
        sign= 1 if a > 0 else -1

        if a * b >= 0:
            while y:
                x,y=x^y,(x&y) << 1
        else:
            while y:
                x,y=x^y, ((~x)& y) << 1

        return x*sign

        