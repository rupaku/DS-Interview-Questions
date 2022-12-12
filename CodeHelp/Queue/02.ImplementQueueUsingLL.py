'''
https://www.codingninjas.com/codestudio/problems/queue-using-array-or-singly-linked-list_2099908?leftPanelTab=1
'''
'''
    Time complexity: O(q)
    Space complexity: O(q)

    Where q is the number of queries.
'''

class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.next = None
        
class Queue:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.size = 0
        
    # Function to check if the queue is empty.
    def isEmpty(self):
        
        return self.size == 0
    
    def enqueue(self, data):
        
        # Increase the count of elements present in the List.
        self.size += 1
        
        # Create a new node.
        newNode = Node(data)
        
        # Check if the Queue is empty.
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return 
        
        # Push the element to the last of the queue.
        self.tail.next = newNode
        self.tail = newNode
        return 
    
    def dequeue(self):
        
        # Check if the queue is empty.
        if self.isEmpty():
            return -1
        
        ans = self.head.data
        
        tmp = Node(self.head)
        self.head = self.head.next
        
        # If the queue is empty make the tail pointer null.
        if self.head == None:
            self.tail = None
            
        tmp = None
        self.size -= 1
        
        return ans
    
    def front(self):
        
        # Check if the queue is empty.
        if self.isEmpty():
            return -1
        
        # Return the element at the front.
        return self.head.data
        
        
        
            