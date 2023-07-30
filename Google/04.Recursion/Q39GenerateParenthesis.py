'''
https://leetcode.com/problems/generate-parentheses/solution/
 We can do this by keeping track of the number of opening 
 and closing brackets we have placed so far.

 We can start an opening bracket if we still have one
 (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtrack(s=[],l=0,r=0):
            if len(s) == 2*n:
                ans.append("".join(s))
                return
            
            if l < n:
                s.append("(")
                backtrack(s,l+1,r)
                s.pop()
            if r < l:
                s.append(")")
                backtrack(s,l,r+1)
                s.pop()
        backtrack()
        return 
        
        