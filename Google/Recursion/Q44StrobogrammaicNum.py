'''
https://leetcode.com/explore/interview/card/google/62/recursion-4/399/
create mapping dict with num with 180 equal and another dict without reverse
check index in mapping handle center 0 condition
'''
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def recursion(index,so_far):
            if index == n:
                self.res.append(so_far)
                return
            
            for i in range(10):
                if i in self.mapping:
                    #handle 0
                    if index == 0 and index < n-1 and i==0:
                        continue
                    #handle center when n is odd
                    if index == n//2 and n%2 == 1 and i not in self.center_candidates:
                        continue
                    if index < n-index or self.mapping[i] == int(so_far[n-index-1]):
                        recursion(index+1, so_far + str(i))
                    
        self.res=[]
        self.center_candidates={0,1,8}
        self.mapping ={0:0,1:1,6:9,9:6,8:8}
        recursion(0,'')
        return self.res
        
        