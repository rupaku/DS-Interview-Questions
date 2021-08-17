'''
https://leetcode.com/problems/delete-nodes-and-return-forest/
https://www.youtube.com/watch?v=R02G113_mFU
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def dfs(node):
            if not node:
                return
            node.left=dfs(node.left)
            node.right=dfs(node.right)
            if node.val in set(to_delete):
                if node.left:
                    output.append(node.left)
                if node.right:
                    output.append(node.right)
                return None
            return node
        if not root:
            return []
        to_delete_set=set(to_delete)
        output=[]
        if root.val not in to_delete_set:
            output.append(root)
        dfs(root)
        return output