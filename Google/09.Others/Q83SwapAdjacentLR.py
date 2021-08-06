'''
https://leetcode.com/explore/interview/card/google/66/others-4/3103/
'''
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # Same number of L and R
        if start.replace('X', '') != end.replace('X', ''):
            return False
        # L can only move left and R can only move right
        l_start = [i for i, c in enumerate(start) if c == 'L']
        r_start = [i for i, c in enumerate(start) if c == 'R']
        l_end = [i for i, c in enumerate(end) if c == 'L']
        r_end = [i for i, c in enumerate(end) if c == 'R']
        if any(l_start[i] < l_end[i] for i in range(len(l_start))):
            return False
        if any(r_start[i] > r_end[i] for i in range(len(r_start))):
            return False
        return True