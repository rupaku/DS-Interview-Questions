'''
https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.arr = []
        self.traversal(root)
        
        return self.arr
    
    def traversal(self, root):
        if root:
            self.traversal(root.left)            
            self.arr.append(root.val)
            self.traversal(root.right)