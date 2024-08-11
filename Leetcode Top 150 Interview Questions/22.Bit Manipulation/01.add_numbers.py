# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2)
        y=int(b,2)
        while y:
            ans=x^y
            carry=(x&y) << 1
            x,y=ans,carry
            
        return bin(x)[2:]
        