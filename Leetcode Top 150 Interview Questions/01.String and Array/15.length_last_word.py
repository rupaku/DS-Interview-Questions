# https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''words = s.strip().split()
        if not words:
            return 0
        return len(words[-1])'''

        n=len(s)-1
        while n >= 0 and s[n] == ' ':
            n = n-1
        
        last_ind = n #beg of last word
        while n >= 0 and s[n] != ' ':
            n = n-1
        
        return last_ind - n
        