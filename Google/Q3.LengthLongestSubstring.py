'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        max_length=0
        mp={}
        start=0
        for i in range(n):
            #if existing key
            if s[i] in mp and start <= mp[s[i]]:
                start = mp[s[i]]+1
            else:
                max_length =max(max_length,i-start+1)
            mp[s[i]] =i
        return max_length
                
                