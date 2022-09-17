'''
https://leetcode.com/problems/transpose-matrix/submissions/
time  O(r*c)
space O(r*c)
'''
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        for i in range(len(matrix[0])):
            temp=[]
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            res.append(temp)
        return res
        