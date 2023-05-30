'''https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solutions/'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root):
            if root:
                yield from inorder(root.left)
                yield root.val
                yield from inorder(root.right)
        nums=[x for x in inorder(root)]
        low=0
        high=len(nums)-1
        while low < high:
            num=nums[low]+nums[high]
            if num == k:
                return True
            elif num < k:
                low=low+1
            else:
                high=high-1
        return False