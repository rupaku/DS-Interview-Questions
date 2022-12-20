'''
https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1
'''
class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self, root1, root2):
        
        #if both nodes are null then we return true.
        if root1 is None and root2 is None:
            return 1
        
        if root1 is not None and root2 is not None:
            
            #we check if data at both nodes and left and right subtree of
            #both the nodes are equal then we return true else return false.
            if(root1.data!=root2.data):
                return 0
                
            return self.isIdentical(root1.left,root2.left) and self.isIdentical(root1.right,root2.right)