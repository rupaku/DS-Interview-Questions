'''
https://www.codingninjas.com/codestudio/problems/largest-bst-subtree_893103?leftPanelTab=1
'''
'''
    Time Complexity: O(N)
    Space Complexity: O(N)
    
    where N is the total number of nodes in the binary tree.
'''


class info:
    def __init__(self):
        self.isValid = True
        self.size = 0
        self.min = 1e9
        self.max = -1e9

    def __del__(self):
        del self


def maxSize(currNode, maxBST):

    if currNode == None:
        newInfo = info()
        return newInfo


    # Information of left and right subtrees.
    left = maxSize(currNode.left, maxBST)
    right = maxSize(currNode.right, maxBST)


    currInfo = info()

    # Size of current subtree.
    currInfo.size = left.size + right.size + 1
    
    # Left and Right subtrees must be BST.
    currInfo.isValid = left.isValid & right.isValid
    
    # Current subtree must form a BST.
    currInfo.isValid &= (currNode.data > left.max)
    currInfo.isValid &= (currNode.data < right.min)
    
    # Updating min and max for current subtree.
    currInfo.min = min(min(left.min, right.min), currNode.data)
    currInfo.max = max(max(left.max, right.max), currNode.data)


    if currInfo.isValid == True:
        maxBST[0] = max(maxBST[0], currInfo.size)

    return currInfo


def largestBST(root):
    
    # Passing 'maxBST' by reference.
    maxBST = [0]
    maxSize(root, maxBST)

    return maxBST[0]