'''
https://www.codingninjas.com/codestudio/problems/kth-smallest-node-in-bst_920441?leftPanelTab=1
'''
'''
    Time Complexity : O(N)
    Space Complexity : O(N)

    Where 'N' is the number of nodes in the given binary search tree.
'''

nodes = []

def inorder(root):
    global nodes

    if (root == None):
        
        #  Base case.
        return

    #  Recur for the left subtree.
    inorder(root.left)

    #  Store the current node value in "nodes".
    nodes.append(root.data)

    #  Recur for the right subtree.
    inorder(root.right)

def kthSmallest(root, k):
    
    global nodes

    #  To store the inorder traversal of the BST.
    nodes = []

    inorder(root)

    return nodes[k - 1]
