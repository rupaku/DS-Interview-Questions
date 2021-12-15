'''
https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End
'''
# This is an input class. Do not edit.
# O(n) | O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    counter=1
	first=head
	second=head
	while counter <= k:
		second = second.next
		counter += 1
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while second.next is not None:
		second= second.next
		first=first.next
	first.next =first.next.next
