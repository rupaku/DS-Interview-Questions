'''
https://www.codingninjas.com/codestudio/problems/normal-bst-to-balanced-bst_920472?leftPanelTab=1
'''
'''

    Time Complexity : O(N)
    Space Complexity : O(N)

    Where N is the number of nodes in BST.

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

# Inorder traversal of the tree.
def inorder(root, inorderArray):
    if root == None:
        return

    inorder(root.left, inorderArray)
    inorderArray.append(root.data)
    inorder(root.right, inorderArray)


def bst(inorderArray, start, end):
    if start > end:
        return None

    # Get the middle of the array and make it as the new root.
    mid = (start + end) // 2

    root = TreeNode(inorderArray[mid])

    # Make the left half of array as the left subtree.
    root.left = bst(inorderArray, start, mid - 1)

    # Make the right half of array as the right subtree.
    root.right = bst(inorderArray, mid + 1, end)

    return root


def balancedBst(root):
    # Array to store the nodes in the order of inorder traversal.
    inorderArray = []

    inorder(root, inorderArray)

    return bst(inorderArray, 0, len(inorderArray) - 1)