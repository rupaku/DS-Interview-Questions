'''
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=len(haystack)
        n=len(needle)
        
        if n == 0:
            return 0
        if h < n:
            return -1
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
            
        return -1
        
        