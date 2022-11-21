'''
https://www.codingninjas.com/codestudio/problems/stack-implementation-using-array_3210209?leftPanelTab=1
'''
'''
    Time complexity: O(1)
    Space complexity: O(N)
    
    Where 'N' is the capacity of the stack.
'''

# Stack class.
class Stack:
    
    def __init__(self, n: int):
        
        # Declare array.
        self.myStack = [0 for _ in range(n)]
        
        # Stack size.
        self.Size = -1
        
        # Maximum size.
        self.n = n

    # Push function.
    def push(self, num: int) -> None:
        
        # Check if stack is not full.
        if self.Size != self.n - 1:
            
            # Increment stack size and update array.
            self.Size += 1
            self.myStack[self.Size] = num

    # Pop function.
    def pop(self) -> int:
        
        # Check if stack is not empty.
        if self.Size != -1:
            
            # Decrease size and return element.
            self.Size -= 1
            return self.myStack[self.Size + 1]
        else:
            return -1

    # Top function.
    def top(self) -> int:
        
        # Check if stack is not empty.
        if self.Size != -1:
            
            # Return element.
            return self.myStack[self.Size]
        else:
            return -1

    # To check whether stack is empty or not.
    def isEmpty(self) -> int:
        
        # Check if stack is not empty.
        if self.Size != -1:
            
            # Return element.
            return 0
        else:
            return 1
        
    # To check whether stack is full or not.
    def isFull(self) -> int:
        
        # Check if stack is not empty.
        if self.Size != self.n - 1:
            
            # Return element.
            return 0
        else:
            return 1
