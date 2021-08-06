'''
https://leetcode.com/explore/interview/card/google/66/others-4/477/
https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/472169/Python-DP
https://www.youtube.com/watch?v=zvqJMGWjuX0
'''
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        M= len(matrix)
        N=len(matrix[0])
        self.empty=False
        if M == 0 or N == 0:
            self.empty=True
            
        else:
            self.dp=[[0 for i in range(N+1)] for j in range(M+1)]
            # print(self.dp)
            # [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0,                   0], [0, 0, 0, 0, 0, 0]]
            
            for i in range(1,M+1):
                for j in range(1,N+1):
                    #cumulative sum of each row
                    self.dp[i][j]= self.dp[i-1][j]+self.dp[i][j-1]- self.dp[i-1][j-1] + matrix[i-1][j-1]
                

    def update(self, row: int, col: int, val: int) -> None:
        for i in range(row+1, len(self.dp)):
            for j in range(col+1, len(self.dp[0])):
                if i == row+1 and j == col+1:
                    prev = self.dp[i][j] -self.dp[i-1][j]-self.dp[i][j-1]+ self.dp[i-1][j-1] 
                    # print(prev) #0
                    diff = val-prev
                    # print(diff) #2
                    self.dp[i][j] = self.dp[i-1][j]+self.dp[i][j-1]- self.dp[i-1][j-1] + val
                else:
                    self.dp[i][j]+=diff   
                    
        # print(self.dp)
        #[[0, 0, 0, 0, 0, 0], [0, 3, 3, 4, 8, 10], [0, 8, 14, 18, 24, 27], [0, 9, 17, 21, 28, 36], [0, 13, 22,              28, 36, 51], [0, 14, 23, 32, 40, 60]]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.empty:
            return 0 
        
        sub1 = self.dp[row1-1+1][col2+1]
        sub2 = self.dp[row2+1][col1+1-1] - self.dp[row1-1+1][col1+1-1]
        return self.dp[row2+1][col2+1] - sub1 - sub2
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)