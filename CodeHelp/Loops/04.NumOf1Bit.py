'''
https://leetcode.com/problems/number-of-1-bits/submissions/
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while (n!=0):
            if n&1: # if last digit is 1, and with 1 will give same
                count=count+1
            n=n>>1
        return count
         