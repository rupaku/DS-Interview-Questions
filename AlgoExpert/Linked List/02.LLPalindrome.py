'''
https://www.algoexpert.io/questions/Linked%20List%20Palindrome
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    # Write your code here.
    slow = head
	fast =  head
	while fast is not None and fast.next is not None:
		slow=slow.next
		fast=fast.next.next
	reverse_sec_half = reverse_LL(slow)
	firstHalfNode = head
	while reverse_sec_half is not None:
		if reverse_sec_half.value != firstHalfNode.value:
			return False
		reverse_sec_half = reverse_sec_half.next
		firstHalfNode = firstHalfNode.next
	return True

def reverse_LL(head):
	prev_node = None
	curr_node = head
	while curr_node is not None:
		next_node = curr_node.next
		curr_node.next = prev_node
		prev_node = curr_node
		curr_node = next_node
	return prev_node