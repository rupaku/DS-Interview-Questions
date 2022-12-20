'''
https://www.codingninjas.com/codestudio/problems/count-leaf-nodes_893055?leftPanelTab=1
'''
'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the total number of nodes in the given Binary Tree.
'''

def noOfLeafNodes(root):

    if root is None:
        return 0

    if (root.left is None and root.right == None):
        return 1

    else:
        count = 0
        count = noOfLeafNodes(root.left) + noOfLeafNodes(root.right)
        return count

