'''
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
'''

from typing import DefaultDict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n=len(s)
        if n < 3:
            return n
        l=0
        r=0
        hashmap=DefaultDict()
        max_len=2
        while r < n:
            # when sliding window has less than 3 characters
            hashmap[s[r]] =r
            r =r+1
            
            #SW 3 characters
            if(len(hashmap) == 3):
                #delete leftmost
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                
                #move left pointer of slidewindow
                l = del_idx+1
                
            max_len=max(max_len,r-l)
        return max_len