# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_gain =max(max_gain(node.left),0)
            right_gain = max(max_gain(node.right),0)
            
            price_newpath = node.val + left_gain + right_gain
            
            max_sum = max(max_sum,price_newpath)
            
            return node.val +max(left_gain,right_gain)
             
        
        max_sum = float('-inf')
        max_gain(root)
        return max_sum
        