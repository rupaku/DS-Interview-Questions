'''
https://leetcode.com/problems/number-of-closed-islands/submissions/
'''
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res+= not grid[i][j] and self.dfs(i,j,grid)

        return res


    def dfs(self,i,j,grid):
        if not (0<=i<len(grid) and 0<=j<len(grid[0])):
            return False
        if grid[i][j]:
            return True

        grid[i][j]=1
        up=self.dfs(i-1,j,grid)
        down=self.dfs(i+1,j,grid)
        left=self.dfs(i,j-1,grid)
        right=self.dfs(i,j+1,grid)

        return (up and down and left and right)