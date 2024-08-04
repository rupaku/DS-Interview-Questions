#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def delete_invalid_string(s, open_symbol, close_symbol):
            stack=[]
            balance=0
            for char in s:
                if char == open_symbol:
                    balance=balance+1
                if char == close_symbol:
                    if balance == 0:
                        continue
                    balance=balance-1
                stack.append(char)
            return "".join(stack)

        s=delete_invalid_string(s,"(",")")
        s=delete_invalid_string(s[::-1],")","(")
        return s[::-1]
         

