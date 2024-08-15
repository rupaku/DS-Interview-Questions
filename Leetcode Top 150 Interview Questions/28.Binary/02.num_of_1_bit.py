# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        #convert least significatant 1 it to 0 till it becomes 0
        count=0
        while (n!=0):
            count=count+1
            n=n & (n-1)
        return count
        