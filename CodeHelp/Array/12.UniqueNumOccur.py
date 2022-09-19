'''
https://leetcode.com/problems/unique-number-of-occurrences/submissions/
'''
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=Counter(arr)
        occur =set()
        for value in counter.values():
            if value in occur:
                return False
            occur.add(value)
        return True