'''
https://practice.geeksforgeeks.org/problems/k-sum-paths/1
'''
class Solution:
    
    def __init__(self):
        self.res = 0
        self.summap = {}
    
    def comparesum(self,root,k,curr_sum=0):
        if root!=None:
            if curr_sum + root.data == k:
                self.res += 1
            
            val = curr_sum + root.data - k
            if val in self.summap:
                self.res += self.summap[val]
            
            tsum = curr_sum + root.data
            if tsum not in self.summap:
                self.summap[tsum] = 0
            self.summap[tsum] += 1
            
            self.comparesum(root.left,k,tsum)
            self.comparesum(root.right,k,tsum)
            
            self.summap[tsum] -= 1
            
            
    
    def sumK(self,root,k):
        if root==None:
            return 0
        self.comparesum(root,k)
        return self.res