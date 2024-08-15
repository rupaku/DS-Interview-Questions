# https://leetcode.com/problems/palindromic-substrings/description/


class Solution:
    def center_count(self,s,l,r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l=l-1
            r=r+1
            self.count=self.count+1
        return self.count

    def countSubstrings(self, s: str) -> int:
        self.count=0
        for i in range(len(s)):
            self.center_count(s,i,i)
            self.center_count(s,i,i+1)
        return self.count

        