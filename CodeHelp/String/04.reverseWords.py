'''
https://leetcode.com/problems/reverse-words-in-a-string-ii/submissions/
'''
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse_helper(left, right):
            nonlocal s
            
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            
        
        reverse_helper(0, len(s) - 1)
        
        
        n = len(s)
        start = end = 0
        
        while start < n:
            while end < n and s[end] != ' ':
                end += 1
            reverse_helper(start, end-1)
            start = end + 1
            end += 1
            
            