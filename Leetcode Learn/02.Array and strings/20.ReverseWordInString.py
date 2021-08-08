
'''
https://leetcode.com/problems/reverse-words-in-a-string/submissions/
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
        