# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=len(haystack)
        n=len(needle)
        if n == 0:
            return 0
        if h < n:
            return -1
        for i in range(h+n-1):
            if haystack[i:i+n] == needle:
                return i
        
        return -1