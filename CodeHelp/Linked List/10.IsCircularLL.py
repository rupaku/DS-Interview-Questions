'''
https://www.geeksforgeeks.org/check-if-a-linked-list-is-circular-linked-list/
O(n)
O(1)
'''
class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
 
def Circular(head):
    if head == None:
        return True
 
    # Next of head
    temp = head.next
    i = 0
 
    # This loop would stop in both cases (1) If
    # Circular (2) Not circular
    while((temp is not None) and (temp is not head)):
        i = i + 1
        temp = temp.next
 
    return(temp == head)
 
 
# Driver's code
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
 
    llist.head.next = second
    second.next = third
    third.next = fourth
 
    if (Circular(llist.head)):
        print('Yes')
    else:
        print('No')
 
    fourth.next = llist.head
 
    if (Circular(llist.head)):
        print('Yes')
    else:
        print('No')
 