'''
https://practice.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/1
'''

class Solution:
    def diagonal(self,root): 
        def diagonalUtil(root, d, diagonalMap):
            if root is None: 
                return
            try : 
                diagonalMap[d].append(root.data) 
            except KeyError: 
                diagonalMap[d] = [root.data] 
            diagonalUtil(root.left, d+1, diagonalMap) 
            diagonalUtil(root.right, d, diagonalMap) 
        diagonalMap = dict() 
        diagonalUtil(root, 0, diagonalMap) 
        diagonalNode = []
        for i in diagonalMap: 
            for j in diagonalMap[i]: 
                diagonalNode.append(j)
        return diagonalNode