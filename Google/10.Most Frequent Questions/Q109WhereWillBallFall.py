'''
https://leetcode.com/problems/where-will-the-ball-fall/submissions/
https://www.youtube.com/watch?v=HeGDdUvNDNc
'''
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row=len(grid)
        col=len(grid[0])
        ans=list(range(col))
        for r in range(row):
            for i in range(col):
                c=ans[i]
                if c == -1:
                    continue
                c_next=c+grid[r][c]
                if c_next < 0 or c_next >= col or grid[r][c_next] == -grid[r][c]:
                    ans[i] =-1
                    continue
                ans[i] += grid[r][c]
        return ans                
        
        