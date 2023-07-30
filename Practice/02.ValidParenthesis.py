'''
https://leetcode.com/problems/valid-parentheses/editorial/
[o(n), o(n)]
'''
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack=[]
        for char in s:
            if char in mapping:
                top_ele=stack.pop() if stack else "#"
                if top_ele != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack
