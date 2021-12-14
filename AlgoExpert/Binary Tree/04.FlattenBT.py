'''
https://www.algoexpert.io/questions/Flatten%20Binary%20Tree
'''
# This is the class of the input root. Do not edit it.
# O(n) |O(d)
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    # Write your code here.
    leftmost,_ = flattenTree(root)
	return leftmost

def flattenTree(node):
	if node.left is None:
		leftmost=node
	else:
		leftsubtreeleftmost, leftsubtreerightmost = flattenTree(node.left)
		connectNode(leftsubtreerightmost, node)
		leftmost = leftsubtreeleftmost
	if node.right is None:
		rightmost = node
	else:
		rightsubtreeleftmost, rightsubtreerightmost = flattenTree(node.right)
		connectNode(node,rightsubtreeleftmost)
		rightmost = rightsubtreerightmost
	return [leftmost,rightmost]

def connectNode(left,right):
	left.right = right
	right.left = left