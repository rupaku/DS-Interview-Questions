'''
https://www.geeksforgeeks.org/reverse-a-linked-list-in-groups-of-given-size/
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def reverse(self,head, k):
        if head == None:
            return None
        next=None
        prev=None
        curr=head
        count=0
        while (curr is not None and count < k):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            count=count+1
        
        if next is not None:
            head.next=self.reverse(next,k)

        return prev
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
 
 
# Driver program
llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
 
print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)
 
print ("\nReversed Linked list")
llist.printList()