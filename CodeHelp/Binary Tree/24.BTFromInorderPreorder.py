'''
https://practice.geeksforgeeks.org/problems/construct-tree-1/1
'''
class Solution:
    def findIndex(self, lst, start, target):
        i = 0
        while lst[start+i] != target:
            i += 1
        return i
    
    def buildUtil(self, inorder, preorder, inStart, preStart, n):
        if n==0:
            return None
        
        ret = Node( preorder[preStart] )
        
        i = self.findIndex( inorder, inStart, preorder[preStart] )
        
        ret.left = self.buildUtil(inorder, preorder, inStart, preStart+1, i)
        
        ret.right = self.buildUtil(inorder, preorder, inStart+i+1, preStart+i+1, n-i-1)
        
        return ret
    
    def buildtree(self, inorder, preorder, n):
        return self.buildUtil(inorder, preorder, 0, 0, n)