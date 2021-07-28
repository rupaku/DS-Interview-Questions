'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3060/
for each string s and t , check # value ,if in new list -> pop , else append to new list
'''

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_list = []
        for c in S:
            if c == '#':
                if s_list:
                    s_list.pop()
            else:
                s_list.append(c)

        t = []
        for c in T:
            if c == '#':
                if t:
                    t.pop()
            else:
                t.append(c)

        return ''.join(s_list) == ''.join(t)