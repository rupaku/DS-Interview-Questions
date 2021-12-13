'''
https://www.algoexpert.io/questions/Validate%20BST
'''
# O(n) | O(d)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return validate_bst_helper(tree,float("-inf"),float("inf"))

def validate_bst_helper(tree,minValue,maxValue):
	if tree is None:
		return True
	if tree.value < minValue or tree.value >= maxValue:
		return False
	leftIsValid = validate_bst_helper(tree.left,minValue,tree.value)
	return leftIsValid and validate_bst_helper(tree.right,tree.value, maxValue)
