'''
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i < j:
            s[i],s[j]=s[j],s[i]
            i=i+1
            j=j-1
        