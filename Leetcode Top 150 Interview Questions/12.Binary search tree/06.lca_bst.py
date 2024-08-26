# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.val > max(p.val,q.val):
            return Solution.lowestCommonAncestor(self,root.left, p, q)
        if root.val < min(p.val,q.val):
            return Solution.lowestCommonAncestor(self, root.right, p, q)
        return root

        