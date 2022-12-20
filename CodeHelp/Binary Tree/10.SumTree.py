'''
https://practice.geeksforgeeks.org/problems/sum-tree/1
'''
class Solution:
    def isleaf(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return 0
    
    def isSumTree(self,root):
        # Code here
        if root is None or self.isleaf(root):
            return 1
        ls = rs = 0
        if self.isSumTree(root.left) and self.isSumTree(root.right):
            if root.left is None:
                ls = 0
            elif self.isleaf(root.left):
                ls = root.left.data
            else:
                ls = 2*root.left.data
    
            if root.right is None:
                rs = 0
            elif self.isleaf(root.right):
                rs = root.right.data
            else:
                rs =2*root.right.data
            return root.data==ls+rs
        return 0