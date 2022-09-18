'''
https://leetcode.com/problems/number-complement/submissions/
'''
class Solution:
    def findComplement(self, n: int) -> int:
        if n == 0:
            return 1
        bit=1
        while n >= bit:
            n=n^bit
            bit=bit <<1
        return n