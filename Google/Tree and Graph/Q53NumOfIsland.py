'''
https://leetcode.com/problems/number-of-islands/submissions/
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        H=len(grid)
        if H == 0:return 0
        W=len(grid[0])
        if W == 0: return 0
        count=0
        for i in range(0,H):
            for j in range(0,W):
                if grid[i][j] == '1':
                    count=count+1
                    self.dfs(grid,i,j)
                    
        return count
    
    def dfs(self,grid:List[List[str]],i,j):
        grid[i][j]='0'
        if i+1 < len(grid) and grid[i+1][j] == '1':
            self.dfs(grid,i+1,j)
        if i-1 >= 0 and grid[i-1][j] == '1':
            self.dfs(grid,i-1,j)
        if j-1 >= 0 and grid[i][j-1] == '1':
            self.dfs(grid,i,j-1)
        if j+1 < len(grid[0]) and grid[i][j+1] == '1':
            self.dfs(grid,i,j+1)
            
        