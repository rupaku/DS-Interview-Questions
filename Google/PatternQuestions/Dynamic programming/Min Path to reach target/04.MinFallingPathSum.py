'''https://leetcode.com/problems/minimum-falling-path-sum/submissions/965694908/'''
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        path=[[0 for i in range(n)] for i in range(n)]
        path[0]=grid[0]
        for i in range(1,n):
            for j in range(n):
                if 0 < j < n-1:
                    path[i][j] = min(path[i-1][j-1], path[i-1][j],path[i-1][j+1]) +grid[i][j]
                elif j == 0:
                    path[i][j] = min(path[i-1][j], path[i-1][j+1]) + grid[i][j]
                else:
                    path[i][j] = min(path[i-1][j],path[i-1][j-1] ) + grid[i][j]
                    
        return min(path[-1])