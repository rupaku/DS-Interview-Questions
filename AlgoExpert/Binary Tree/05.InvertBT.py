'''
https://www.algoexpert.io/questions/Invert%20Binary%20Tree
'''
def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
		return
	swap_left_and_right(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

def swap_left_and_right(tree):
	tree.left,tree.right = tree.right, tree.left
	
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
