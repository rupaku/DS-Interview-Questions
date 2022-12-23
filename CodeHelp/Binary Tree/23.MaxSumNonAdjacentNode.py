'''
https://practice.geeksforgeeks.org/problems/maximum-sum-of-non-adjacent-nodes/1
'''
class Solution:
    #Function which returns a pair such that first of the pair indicates maximum 
    #sum when data of a node is included and the second when it is not included.
    def maxSumHelper(self, root) :
        
        #if root is null, we return two zeroes in pair.
        if (root == None):  
            sum = [0, 0]  
            return sum
            
        #calling function recursively for left and right subtrees.
        sum1 = self.maxSumHelper(root.left)  
        sum2 = self.maxSumHelper(root.right)  
        sum = [0, 0] 
        
        #current node is included (Left and right children are not included).
        sum[0] = sum1[1] + sum2[1] + root.data 
        
        #current node is excluded (Either left or right child is included).
        sum[1] = (max(sum1[0], sum1[1]) + max(sum2[0], sum2[1]))
        return sum
    
    
    #Function to return the maximum sum of non-adjacent nodes.  
    def getMaxSum(self, root) : 
      
        res = self.maxSumHelper(root) 
        #returning the maximum between the elements in pair(res).
        return max(res[0], res[1])