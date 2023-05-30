'''https://leetcode.com/problems/sum-of-square-numbers/description/
'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low=0
        high=int(c**0.5)
        while low <= high:
            num=low**2+high**2
            if num == c:
                return True
            elif num < c:
                low=low+1
            else:
                high=high-1
        return False