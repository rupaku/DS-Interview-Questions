# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            def array_to_tree(left,right):
                if left > right:
                    return None
                
                root_value = postorder.pop() #pop from last of postorder
                root= TreeNode(root_value)
                
                #first right then left
                root.right = array_to_tree(inorder_index_map[root_value]+1, right)
                root.left = array_to_tree(left, inorder_index_map[root_value]-1)

                return root

            inorder_index_map={}
            for i,val in enumerate(inorder):
                inorder_index_map[val]=i

            return array_to_tree(0,len(inorder)-1)
