'''
https://www.algoexpert.io/questions/Find%20Loop
'''
# This is an input class. Do not edit.
#On(n) |O(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def findLoop(head):
    # Write your code here.
    first=head.next
	sec = head.next.next
	while first != sec:
		first=first.next
		sec= sec.next.next
	first = head
	while first != sec:
		first = first.next
		sec= sec.next
	return first
