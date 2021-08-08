'''
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s[::-1].split()))
        