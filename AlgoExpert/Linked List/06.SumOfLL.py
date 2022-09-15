'''
https://www.algoexpert.io/questions/Sum%20of%20Linked%20Lists
'''

# O(max(n,m)) | O(max(n,m))# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None 


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    newLLHeadPointer = LinkedList(0)
	curr_node = newLLHeadPointer
	carry = 0
	
	node1 = linkedListOne
	node2 = linkedListTwo
	while node1 is not None or node2 is not None or carry != 0:
		value1 = node1.value if node1 is not None else 0
		value2 = node2.value if node2 is not None else 0
		sum_of_value = value1 + value2 + carry
		new_value = sum_of_value % 10
		new_node = LinkedList(new_value)
		curr_node.next = new_node
		curr_node = new_node
		
		carry = sum_of_value // 10
		node1 = node1.next if node1 is not None else None
		node2 = node2.next if node2 is not None else None
	return newLLHeadPointer.next
