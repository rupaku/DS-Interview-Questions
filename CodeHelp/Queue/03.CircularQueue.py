'''
https://www.codingninjas.com/codestudio/problems/circular-queue_1170058?leftPanelTab=1
'''
"""
    Time complexity: O(1) for all operations.
    Space Complexity: O(N)
    
    Where 'N' is the size of the queue. 
"""

class CircularQueue:
    def __init__(self, n):
        self.d = n

        # For a circular queue the front and rear both start as empty.
        self.front = -1
        self.rear = -1

        # Create the arrays.
        self.arr = [-1 for i in range(self.d)]

    # Enqueues 'X' into the queue. Returns true if it gets pushed into the queue, and false otherwise.
    def enqueue(self, value):
        if ((self.front == 0 and self.rear == self.d - 1) or (self.rear == (self.front - 1) % (self.d - 1))): 
            """
               If the queue is full, no more elements can be added so return false.
               Queue will be full if front is at 1st element and rear is at last element.
               OR if rear is equal to front - 1.
            """
            return False
         
        elif (self.front == -1):  
            # Queue is empty, hence insert the first element.
            self.front = self.rear = 0
            self.arr[self.rear] = value
         
        elif (self.rear == self.d - 1 and self.front != 0):  
            # If self.rear reaches end of queue but the first element is empty.
            self.rear = 0 
            self.arr[self.rear] = value
         
        else:
            # Otherwise simply enqueue the element.
            self.rear += 1
            self.arr[self.rear] = value
         
        return True

    # Dequeues pop element from queue. Returns -1 if the queue is empty, otherwise returns the popped element.
    def dequeue(self):
        if (self.front == -1): 
            # If queue is empty.
            return -1
  
        # Initialise element to store dequeud element.
        data = self.arr[self.front]
        self.arr[self.front] = -1
        
        if (self.front == self.rear): 
            # If the queue has only one element.
            self.front = -1
            self.rear = -1 
         
        elif (self.front == self.d - 1):
            # If self.front is the last element of the queue.
            self.front = 0
        
        else:
            # In all other cases simply dequeue.
            self.front += 1
        
        # Return the dequeued element.
        return data