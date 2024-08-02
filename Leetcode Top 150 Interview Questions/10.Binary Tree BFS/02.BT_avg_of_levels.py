# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
       #BFS
        if root is None:
            return []

        queue=deque([root])
        avg=[]
       

        while queue:
            level_len = len(queue)
            sm=0

            for i in range(level_len):
                node=queue.popleft()

                sm=sm + node.val 
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg.append(sm/level_len)

        return avg
        