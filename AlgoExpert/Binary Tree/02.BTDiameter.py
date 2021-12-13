'''
https://www.algoexpert.io/questions/Binary%20Tree%20Diameter
'''
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(0,0)
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
	maxDiameterSoFar =max(leftTreeInfo.diameter, rightTreeInfo.diameter)
	currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
	currentHeight = 1 +max(leftTreeInfo.height,rightTreeInfo.height)
	return TreeInfo(currentDiameter, currentHeight)
	
class TreeInfo:
	def __init__(self,diameter,height):
		self.diameter=diameter
		self.height=height
