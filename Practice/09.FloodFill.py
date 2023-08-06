'''https://leetcode.com/problems/flood-fill/'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R = len(image)
        C=len(image[0])
        color=image[sr][sc]
        if color == newColor:
            return image
        def dfs(sr,sc):
            if image[sr][sc] == color:
                image[sr][sc] = newColor
                if sr >= 1:
                    dfs(sr-1,sc)
                if sr+1 < R:
                    dfs(sr+1,sc)
                if sc >= 1:
                    dfs(sr,sc-1)
                if sc+1 < C: 
                    dfs(sr,sc+1)
        dfs(sr,sc)
        return image