'''
https://leetcode.com/problems/decode-string/submissions/
'''
class Solution:
    def decodeString(self, s: str) -> str:
        curr_str=''
        num=0
        stack=[]
        for c in s:
            if c.isdigit():
                num=num*10+int(c)
            elif c == '[':
                stack.append(num)
                stack.append(curr_str)
                num=0
                curr_str=''
            elif c == ']':
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_str = prev_str + prev_num * curr_str
            else:
                curr_str = curr_str + c
            
        return curr_str