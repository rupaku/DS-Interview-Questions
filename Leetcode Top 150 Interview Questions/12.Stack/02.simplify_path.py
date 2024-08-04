# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        for char in path.split("/"):
            if char == "..":
                if stack:
                    stack.pop()
            elif char == "." or not char:
                continue
            else:
                stack.append(char)

        final_str="/"+"/".join(stack)
        return final_str
        