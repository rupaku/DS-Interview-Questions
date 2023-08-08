'''https://leetcode.com/problems/diameter-of-binary-tree/'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def height(node):
            if not node:
                return 0
            lheight = height(node.left)
            rheight = height(node.right)
            self.ans = max(self.ans, lheight+rheight+1)
            return max(lheight, rheight) + 1

        height(root)
        return self.ans - 1
    
        