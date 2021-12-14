'''
https://www.algoexpert.io/questions/Reverse%20Linked%20List
'''
# This is an input class. Do not edit.
# O(n) | O(1) space
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    prev_node =None
	curr_node=head
	while curr_node is not None:
		next_node = curr_node.next
		curr_node.next = prev_node
		prev_node = curr_node
		curr_node = next_node
	return prev_node
