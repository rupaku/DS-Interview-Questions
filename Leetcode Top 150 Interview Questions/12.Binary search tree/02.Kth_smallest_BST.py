# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(r):
            return inorder(r.left)+[r.val]+inorder(r.right) if r else []
        return inorder(root)[k-1]
        

# class TreeNode:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
        
# class Solution:
#     def insert(root, x):
    
#         if (root == None):
#             return TreeNode(x)
#         if (x < root.val):
#             root.left = Solution.insert(root.left, x)
#         elif (x > root.val):
#             root.right = Solution.insert(root.right, x)
#         return root
    
#     def inorder(self,root):
#         return inorder(root.left)+[root.val]+ inorder(root.right) if root else []
        
#     def kth_smallest(self, root , k):
#         return inorder(root)[k-1]
        
# if __name__ == "__main__":
#     ls = [3,1,4,None,2]
#     root= None
#     k = 1
#     obj= Solution()
#     for x in ls:
#         root=Solution.insert(root,x)
#     print(root)
        
#     res=obj.kth_smallest(root,k)
#     print(res)