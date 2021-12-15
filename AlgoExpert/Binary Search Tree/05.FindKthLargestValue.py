'''
https://www.algoexpert.io/questions/Find%20Kth%20Largest%20Value%20In%20BST
'''
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    sortedNodeValues = []
	inorder_traverse(tree, sortedNodeValues)
	return sortedNodeValues[len(sortedNodeValues)-k]

def inorder_traverse(node,sortedNodeValues):
	if node is None:
		return
	inorder_traverse(node.left,sortedNodeValues)
	sortedNodeValues.append(node.value)
	inorder_traverse(node.right,sortedNodeValues)
