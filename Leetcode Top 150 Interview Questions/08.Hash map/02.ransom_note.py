# https://leetcode.com/problems/ransom-note/

import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        letters = collections.Counter(magazine)
        for ch in ransomNote:
            if letters[ch] <= 0:
                return False
            letters[ch] -= 1
        return True