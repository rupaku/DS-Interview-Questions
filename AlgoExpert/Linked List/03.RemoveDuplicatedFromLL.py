'''
https://www.algoexpert.io/questions/Remove%20Duplicates%20From%20Linked%20List
'''
# This is an input class. Do not edit.
# O(n) | O(1) time
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    curr_node = linkedList
	while curr_node is not None:
		next_distinct_node = curr_node.next
		while next_distinct_node is not None and next_distinct_node.value == curr_node.value:
			next_distinct_node = next_distinct_node.next
		curr_node.next = next_distinct_node
		curr_node = next_distinct_node
	return linkedList
