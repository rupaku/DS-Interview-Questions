'''
https://leetcode.com/problems/number-of-good-ways-to-split-a-string/submissions/
'''
import collections
class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        right_counter=collections.Counter(s)
        left_set=set()
        ans=0
        for i in range(len(s)-1):
            left_set.add(s[i])
            right_counter[s[i]] -= 1
            if right_counter[s[i]] <= 0:
                del right_counter[s[i]]
            if len(right_counter) == len(left_set):
                ans += 1
        return ans
            
        