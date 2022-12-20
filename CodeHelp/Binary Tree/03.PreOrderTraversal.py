'''
https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/862191395/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []
        self.traversal(root)
        
        return self.arr
    
    def traversal(self, root):
        if root:
            self.arr.append(root.val)
            self.traversal(root.left)            
            self.traversal(root.right)