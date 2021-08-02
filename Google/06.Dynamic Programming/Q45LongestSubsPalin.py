'''
https://leetcode.com/problems/longest-palindromic-substring/solution/
https://www.youtube.com/watch?v=XYQecbcd6_c&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=8
start in middle and expanding outside l=l-1, r=r+1
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0
        # i is center position
        for i in range(len(s)):
            #Odd length
            l=i
            r=i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l=l-1
                r=r+1
            #Even length
            l=i
            r=i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l=l-1
                r=r+1
                    
        return res

                    
         