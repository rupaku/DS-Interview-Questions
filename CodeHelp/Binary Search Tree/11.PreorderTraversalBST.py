'''
https://www.codingninjas.com/codestudio/problems/preorder-traversal-to-bst_893111?leftPanelTab=1
'''
'''
    Time Complexity : O(N)
    Space Complexity : O(N)
    
    Where N denotes number of nodes in the array/list.
'''

class   TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def helper(preorder, preorderIndex, minVal, maxVal):
    if preorderIndex[0] == len(preorder):
        return None

    currVal = preorder[preorderIndex[0]]

    if currVal < minVal or currVal > maxVal:
        return None

    root = TreeNode(currVal)

    preorderIndex[0] += 1

    # Recursivley construct left subtree.
    root.left = helper(preorder, preorderIndex, minVal, currVal - 1)
    
    # Recursivley construct right subtree.
    root.right = helper(preorder, preorderIndex, currVal + 1, maxVal)

    return root


def preorderToBST(preorder):

    # Passing 'preorderIndex' by reference.
    preorderIndex = [0]
    maxVal = 1e9
    minVal = -1e9

    root = helper(preorder, preorderIndex, minVal, maxVal)

    return root