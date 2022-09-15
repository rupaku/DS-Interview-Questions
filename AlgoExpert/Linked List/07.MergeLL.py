'''
https://www.algoexpert.io/questions/Merge%20Linked%20Lists
'''
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    recursive_merge(headOne,headTwo,None)
	return headOne if headOne.value < headTwo.value else headTwo

def recursive_merge(p1,p2,p1Prev):
	if p1 is None:
		p1Prev.next = p2
		return
	if p2 is None:
		return
	if p1.value < p2.value:
		recursive_merge(p1.next,p2,p1)
	else:
		if p1Prev is not None:
			p1Prev.next = p2
		newP2 = p2.next
		p2.next = p1
		recursive_merge(p1,newP2,p2)