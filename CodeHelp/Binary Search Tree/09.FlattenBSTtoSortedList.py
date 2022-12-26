'''
https://www.codingninjas.com/codestudio/problems/flatten-bst-to-a-sorted-list_1169459?leftPanelTab=1
'''
'''
    Time Complexity - O(N)
    Space Complexity - O(H)

    Where N is the total number of nodes in the tree and H is the height of the tree.
'''

class  TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

# Function to copy a tree.
def copyTree(root):

    if root == None:
        return None

    copyRoot = TreeNode(root.data)

    copyRoot.left = copyTree(root.left)
    copyRoot.right = copyTree(root.right)

    return copyRoot

def inorder(root, previous):
    if root == None:
        return

    inorder(root.left, previous)

    previous[0].left = None
    previous[0].right = root
    previous[0] = root

    inorder(root.right, previous)

def flatten(root):

    if root == None:
        return root

    temp = TreeNode(-1)

    # passing the variable by reference
    previous = [temp]

    inorder(root, previous)

    previous[0].left = None
    previous[0].right = None

    # Copy the tree.
    newRoot = copyTree(temp.right)

    del temp

    return newRoot