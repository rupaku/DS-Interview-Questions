'''
https://www.codingninjas.com/codestudio/problems/sort-a-stack_985275?leftPanelTab=1
'''
'''
    Time Complexity: O(N^2)
    Space Complexity: O(N),

    where N is the number of elements in the stack.
'''


def sortedInsert(stack, current):
    if len(stack) == 0 or current > stack[-1]:
        stack.append(current)
        return

    # Remove the top element
    top = stack[-1]
    del stack[-1]

    # Recursion for the remaining elements in the stack
    sortedInsert(stack, current)

    # Insert the popped element back in the stack.
    stack.append(top)


def sortStack(stack):
    # Base Case : If the stack is empty.
    if len(stack) == 0:
        return

    # Remove the top element
    top = stack[-1]
    del stack[-1]

    # Recursion for the remaining elements in the stack
    sortStack(stack)

    # Insert the popped element back in the stack.
    sortedInsert(stack, top)
