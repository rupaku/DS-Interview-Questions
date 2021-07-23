'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        max_length=0
        mp={}
        start=0
        for j in range(n):
            #if existing key
            if s[j] in mp:
                start=max(mp[s[j]],start)
            
            #If new key, add to dictionary
            max_length =max(max_length,j-start+1)
            mp[s[j]] = j+1
        return max_length
                