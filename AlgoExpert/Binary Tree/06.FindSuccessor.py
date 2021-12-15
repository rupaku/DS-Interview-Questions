'''
https://www.algoexpert.io/questions/Find%20Successor
'''
# This is an input class. Do not edit.
#O(n) |O(n)
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    inorder_traversal = get_inorder_traversal(tree)
	for idx, curr_node in enumerate(inorder_traversal):
		if curr_node != node:
			continue
		if idx == len(inorder_traversal) -1:
			return None
		return inorder_traversal[idx+1]
def get_inorder_traversal(node,order =[]):
	if node is None:
		return order
	get_inorder_traversal(node.left,order)
	order.append(node)
	get_inorder_traversal(node.right,order)
	
	return order
