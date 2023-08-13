'''https://leetcode.com/problems/evaluate-reverse-polish-notation/'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
                continue
            
            num_2=stack.pop()
            num_1=stack.pop()

            res=0
            if token == "+":
                res=num_1 + num_2
            elif token == "-":
                res=num_1 - num_2
            elif token == "*":
                res=num_1 * num_2
            elif token == "/":
                res=int(num_1 / num_2)
            stack.append(res)

        return stack.pop()