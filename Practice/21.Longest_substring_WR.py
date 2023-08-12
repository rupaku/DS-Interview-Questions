'''https://leetcode.com/problems/longest-substring-without-repeating-characters/'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        mp={}
        ans=0
        i=0
        for j in range(len(s)):
            if s[j] in mp:
                i=max(mp[s[j]], i)
            ans=max(ans,j-i+1)
            mp[s[j]] =j+1
        return ans
           