'''
https://practice.geeksforgeeks.org/problems/flatten-binary-tree-to-linked-list/1
'''
class Solution:
    def flatten(self, root):
        if root==None or (not root.left and not root.right):
            return
        else :
            #if root.left exists than we have to make it root.right
            if root.left:
                self.flatten(root.left)#first we flatten the left part 
                temp=root.right#storing the root.right in temp
                
                root.right=root.left
                root.left=None
                t=root.right#finding the position to attach the temp part
                while t.right:
                    t=t.right
                t.right=temp#attaching the temp again 
                    
            self.flatten(root.right)#calling the same function now for root.right