'''
https://leetcode.com/problems/delete-columns-to-make-sorted/submissions/
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        for i in range(len(strs[0])):
            temp = [x[i] for x in strs]
            result += 0 if temp == sorted(temp) else 1
        return result