'''
https://www.codingninjas.com/codestudio/problems/delete-middle-element-from-stack_985246?leftPanelTab=2
'''
'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of integers in the stack
'''

def deleteMiddleHelper(inputStack, N, count):

    # Base condition
    if count == N and N == 0:
        inputStack.pop()
        return

    if len(inputStack) == 0 or count == N:
        return

    # Removing current element
    top = inputStack[-1]
    inputStack.pop()
    deleteMiddleHelper(inputStack, N, count + 1)

    # Store the element back in the stack if not middle element
    if count != N // 2:
        inputStack.append(top)


def deleteMiddle(inputStack, N):
    deleteMiddleHelper(inputStack, N, 0)