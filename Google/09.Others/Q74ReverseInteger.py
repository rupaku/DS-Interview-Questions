'''
https://leetcode.com/problems/reverse-integer/submissions/
check if num is in range
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31:
            return 0
        else:
            st=str(x)
            if x >= 0:
                rev=st[::-1]
            else:
                temp=st[1:]
                temp2=temp[::-1]
                rev="-"+temp2
            
            if int(rev) >= 2**31-1 or int(rev) <= -2**31:
                return 0
            else:
                return int(rev)
          