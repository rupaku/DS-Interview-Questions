'''https://leetcode.com/problems/duplicate-zeros/'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1,0)
                i=i+2
                arr.pop()
            else:
                i=i+1
        return arr