'''  https://leetcode.com/problems/pascals-triangle/solution/ 
time  O(n2)
space O(1)
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows   == 0: return []
        elif numRows == 1: return [[1]]
        Tri = [[1]] # result
        for i in range(1,numRows):
            row = [1]
            for j in range(1,i):
                row.append(Tri[i-1][j-1] + Tri[i-1][j]) #for mid num
            row.append(1) # for side 1s
            Tri.append(row)
        return Tri
