'''
https://practice.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1
'''
class Solution:
    def SumOfLongRootToLeafPathUtil(self,root, Sum, Len,maxLen, maxSum):
        # if true, then we have traversed a  
        # root to leaf path  
        if (not root): 
            # update maximum Length and maximum Sum  
            # according to the given conditions  
            if (maxLen[0] < Len):  
                maxLen[0] = Len
                maxSum[0] = Sum
            elif (maxLen[0]== Len and 
                  maxSum[0] < Sum):  
                maxSum[0] = Sum
            return
      
        # recur for left subtree  
        self.SumOfLongRootToLeafPathUtil(root.left, Sum + root.data,  
                                Len + 1, maxLen, maxSum)  
      
        # recur for right subtree  
        self.SumOfLongRootToLeafPathUtil(root.right, Sum + root.data,  
                                Len + 1, maxLen, maxSum) 
  
 
    def sumOfLongRootToLeafPath(self,root):
        # if tree is NULL, then Sum is 0  
        if (not root):  
            return 0
        maxSum = [-999999999999] 
        maxLen = [0]  
      
        # finding the maximum Sum 'maxSum' for  
        # the maximum Length root to leaf path  
        self.SumOfLongRootToLeafPathUtil(root, 0, 0,maxLen, maxSum)  
      
        # required maximum Sum  
        return maxSum[0]