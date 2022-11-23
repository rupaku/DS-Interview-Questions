'''
https://www.codingninjas.com/codestudio/problems/insert-an-element-at-its-bottom-in-a-given-stack_1171166?leftPanelTab=1
'''
'''

    Time Complexity: O(N)
    Space Complexity: O(N),

    Where N is the size of the given stack MY_STACK.    

'''

from collections import deque

def pushAtBottom(myStack: deque, x: int):
    # Base Case
    if (len(myStack) == 0):
        myStack.append(x)
        return myStack

    # Recursive calls 
    num = myStack[len(myStack) - 1]
    myStack.pop()
    pushAtBottom(myStack, x)
    myStack.append(num)

    return myStack