
'''
https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/862191975/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []
        self.traversal(root)
        
        return self.arr
    
    def traversal(self, root):
        if root:
            self.traversal(root.left)            
            self.traversal(root.right)  
            self.arr.append(root.val)
        