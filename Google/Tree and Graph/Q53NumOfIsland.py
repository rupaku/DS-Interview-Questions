'''
https://leetcode.com/problems/number-of-islands/submissions/
'''
#DFS way
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
            
        
# BFS way
class Solution:
    #BFS way
    def numIslands(self, grid: List[List[str]]) -> int:
        H=len(grid)
        if H == 0:return 0
        W=len(grid[0])
        if W == 0: return 0
        count=0
        visit=set()
        def bfs(i,j):
            q=collections.deque()
            visit.add((i,j))  # as tuple 
            q.append((i,j))  # as tuple 
            while q:
                row,col = q.popleft()
                directions =[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    i= row+dr
                    j= col+dc

                    if (i in range(H) and j in range(W) and grid[i][j] == '1' and (i,j) not in visit):
                        visit.add((i,j))  # as tuple 
                        q.append((i,j))  # as tuple 
                        
        for i in range(0,H):
            for j in range(0,W):
                if grid[i][j] == '1' and (i,j) not in visit:
                    bfs(i,j)
                    count=count+1
                    
        return count