# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten_tree(self,node):
        if not node:
            return None

        if not node.left and not node.right:
            return node

        leftTail=self.flatten_tree(node.left)
        rightTail= self.flatten_tree(node.right)

        if leftTail:
            leftTail.right=node.right
            node.right=node.left
            node.left=None

        return rightTail if rightTail else leftTail

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        return Solution.flatten_tree(self,root)
        