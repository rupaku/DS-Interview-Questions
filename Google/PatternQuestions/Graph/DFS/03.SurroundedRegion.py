class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(grid,i,j):
            if grid[i][j] != 'O':
                return
            grid[i][j] ='E'
            if i+1 < len(grid):
                dfs(grid,i+1,j)
            if j+1 < len(grid[0]):
                dfs(grid,i,j+1)
            if i-1 > 0:
                dfs(grid,i-1,j)
            if j-1 > 0:
                dfs(grid,i,j-1)
        if not grid or not grid[0]:
            return
        from itertools import product
        borders = list(product(range(len(grid)), [0, len(grid[0])-1])) \
                + list(product([0, len(grid)-1], range(len(grid[0]))))
        for i, j in borders:
            dfs(grid,i,j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                elif grid[i][j] == 'E':
                    grid[i][j] = 'O'