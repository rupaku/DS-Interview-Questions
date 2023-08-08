'''https://leetcode.com/problems/longest-palindrome/'''
import collections
class Solution:
    def longestPalindrome(self, s):
        pairs=0
        unpaired_chars =set()
        for ch in s:
            if ch in unpaired_chars:
                pairs += 1
                unpaired_chars.remove(ch)
            else:
                unpaired_chars.add(ch)
        return pairs*2 + 1 if unpaired_chars else pairs*2