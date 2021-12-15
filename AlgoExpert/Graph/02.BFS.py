'''
https://www.algoexpert.io/questions/Breadth-first%20Search
'''
# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
#O(V+E) | O(V) space
    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = [self]
		while len(queue) > 0:
			curr = queue.pop(0)
			array.append(curr.name)
			for child in curr.children:
				queue.append(child)
		return array
