'''https://leetcode.com/problems/rotating-the-box/description/'''
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i in range(len(box)):
           l=len(box[0])-1
           r=len(box[0])
           while l >= 0:
                if box[i][l] == "*":
                   r=l
                elif box[i][l] == "#":
                    box[i][r-1],box[i][l]= box[i][l],box[i][r-1]
                    r=r-1
                l=l-1
        #Transpose
        res=[]
        for j in range(len(box[0])):
            row=[]
            for i in range(len(box)-1,-1,-1):
                row.append(box[i][j])
            res.append(row)
        return res