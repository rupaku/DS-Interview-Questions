'''
https://leetcode.com/problems/complement-of-base-10-integer/
'''
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        bit=1
        while n >= bit:
            n=n^bit
            bit=bit <<1
        return n
        