'''https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/'''

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        long_word=""
        for word in d:
            p1=0
            p2=0
            while p1 < len(s) and p2 < len(word):
                if s[p1] == word[p2]:
                    p1=p1+1
                    p2=p2+1
                else:
                    p1=p1+1
            if p2 == len(word):
                if len(word) > len(long_word):
                    long_word=word
                elif len(word) == len(long_word):
                    long_word = min(long_word,word)
        return long_word