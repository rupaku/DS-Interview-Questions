'''
https://leetcode.com/problems/path-sum/submissions/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum=targetSum-root.val
        #if its leaf node
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
         