'''
https://leetcode.com/problems/find-duplicate-subtrees/submissions/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans=[]
        mapping={}
        def dfs(node,path):
            if node:
                path += str(node.val)+"-"+dfs(node.left,path)+"-"+dfs(node.right,path)
                if path in mapping:
                    mapping[path] += 1
                    if mapping[path] == 1:
                        ans.append(node)
                else:
                    mapping[path]=0
                return path
            else:
                return "#"
        
        dfs(root,"")
        return ans
        