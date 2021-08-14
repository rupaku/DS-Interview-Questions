'''
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix) #row
        n = len(matrix[0]) #col
        left = 0 
        right = n-1
        down  = m-1
        top = 0
        direction = 0
        ans = []
        while(left<=right and down>=top):
            
            if direction ==0:
                # go right
                for i in range(left , right+1):
                    ans.append(matrix[top][i])
                top+=1
            elif direction==1:
                #go down
                for j in range(top , down+1):
                    ans.append(matrix[j][right])
                right-=1
            elif direction ==2:
                #go left
                for j in range(right , left-1,-1):
                    ans.append(matrix[down][j])
                down-=1
            elif direction==3:
                #go up 
                for j in range(down , top-1 , -1):
                    ans.append(matrix[j][left])
                left+=1
            
            direction= (direction +1)%4
            
        return ans
                            