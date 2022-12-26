'''
https://www.codingninjas.com/codestudio/problems/two-sum-in-a-bst_1062631?leftPanelTab=1
'''
'''
    Time Complexity: O(N).
    Space Complexity: O(N).

    Where N is the total number of nodes in the tree.
'''


# BinaryTreeNode class definition
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrder(root, inOrderArray):
    # Base Case
    if root == None:
        return

    inOrder(root.left, inOrderArray)
    inOrderArray.append(root.data)
    inOrder(root.right, inOrderArray)


def twoSumInBST(root, target):
    inOrderArray = []

    # This inorder function stores the value of nodes in the vector inorderArray in the inorder traversal.
    inOrder(root, inOrderArray)

    # Keep two pointers i and j at the beginning and at the end of the array respectively.
    i, j = 0, len(inOrderArray) - 1

    while i < j:
        # Finding the sum at the current pointers
        sm = inOrderArray[i] + inOrderArray[j]

        # If the sum is equal to the target value, then return true.
        if sm == target:
            return True
        # If the sum exceeds the target value, then decrement j by 1.
        elif sm > target:
            j -= 1
        # If the sum is less than the target value, then increment i by 1.
        else:
            i += 1

    return False
