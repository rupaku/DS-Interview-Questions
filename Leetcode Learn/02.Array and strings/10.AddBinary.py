'''
https://leetcode.com/problems/add-binary/submissions/
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2)
        y=int(b,2)
        while y:
            ans=x^y
            carry=(x&y) << 1 #left shift of and
            x,y=ans,carry
            
        return bin(x)[2:]
        