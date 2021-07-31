'''
https://leetcode.com/problems/count-complete-tree-nodes/solution/

Return 2^d - 1 + the number of nodes in the last level.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Method 1 Recursion
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.left) +self.countNodes(root.right) if root else 0

-----------------------------------------------------------------------------------------------
#Method 2 Binary Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compute_depth(self,node:TreeNode) -> int:
        d=0
        while node.left:
            node=node.left
            d=d+1
        return d

    def exist(self,index:int,d:int,node:TreeNode) -> bool:
        left=0
        right=2**d -1
        for _ in range(d):
            pivot = left+(right-left)//2
            if index <= pivot:
                node = node.left
                right=pivot
            else:
                node=node.right
                left=pivot+1
        return node is not None
    
    def countNodes(self,root:TreeNode)-> int:
        if not root:
            return 0
        d=self.compute_depth(root)
        if d == 0:
            return 1
        
        left=1
        right=2**d-1
        while left <= right:
            pivot= left+(right-left)//2
            if self.exist(pivot,d,root):
                left=pivot+1
            else:
                right=pivot-1
        return (2**d -1) +left
            
        