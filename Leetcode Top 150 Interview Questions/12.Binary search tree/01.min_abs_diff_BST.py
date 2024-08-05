# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder_nodes_list =[]
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            inorder_nodes_list.append(node.val)
            inorder(node.right)

        inorder(root)

        min_diff = 1e9
        for i in range(1,len(inorder_nodes_list)):
            min_diff = min(min_diff, inorder_nodes_list[i]- inorder_nodes_list[i-1])
        return min_diff
        