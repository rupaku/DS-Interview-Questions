'''
https://www.codingninjas.com/codestudio/problems/n-stacks-in-an-array_1164271?leftPanelTab=1
'''
'''
    Time complexity: O(1) for all operations.
	Space Complexity: O(S + N)
	
	Where S is the size of the array, 
    N is the number of stacks.
'''


class NStack:
    def __init__(self, n, s):
        self.n = n
        self.s = s

        # Array to implement the stacks.
        self.arr = [0 for i in range(s)]

        # Array to keep track of the indices of the top elements of every stack.
        self.top = [-1 for i in range(n)]

        # Initialize all spaces as free as initially the complete array is empty.
        self.next = [i+1 for i in range(s)]

        # Set the last pointer of the free list to -1 to indicate the end of free list.
        self.next[s-1] = -1

        # Initialize the starting index of the free list.
        self.freeStart = 0

    # Pushes 'X' into the Mth stack. Returns true if it gets pushed into the stack, and false otherwise.
    def push(self, x, m):
        if (self.freeStart == -1):
            # Array is full. So, element cannot be inserted.
            return False

        # Store the index of the first free slot in a temporary variable.
        index = self.freeStart

        # Update the starting index of the free list.
        self.freeStart = self.next[index]

        # Store the new element in the free slot.
        self.arr[index] = x

        # Update the next pointer of the new element.
        self.next[index] = self.top[m-1]

        # Add the element to the stack by updating the head/top of the stack list.
        self.top[m-1] = index

        return True

    # Pops top element from Mth Stack. Returns -1 if the stack is empty, otherwise returns the popped element.
    def pop(self, m):
        if (self.top[m - 1] == -1):
            # Stack is empty. So, return -1.
            return -1

        # Find the index of the top element of the stack.
        index = self.top[m - 1]

        # Remove the element from the stack by updating the head/top of the stack list.
        self.top[m - 1] = self.next[index]

        # Add the free slot to the free list.
        self.next[index] = self.freeStart
        self.freeStart = index

        # Return the popped element.
        return self.arr[index]