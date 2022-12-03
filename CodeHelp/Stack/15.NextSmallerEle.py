'''
https://www.codingninjas.com/codestudio/problems/next-smaller-element_1112581?leftPanelTab=1
'''
'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N denotes the number of elements in the array.
'''

def nextSmallerElement(arr, n):

    # Defining the list to store next smaller elements for the array.
    ans = [0 for i in range(n)]

    # Defining the stack and pushing -1 to it.
    stk = []
    stk.append(-1)

    for i in range(n - 1, -1, -1):

        # Removing all the elements greater than or equal to current element from the stack.
        while(stk[-1] >= arr[i]):
            stk.pop()

        # Setting the next smaller element as the element at top of stack.
        ans[i] = stk[-1]

        # Pushing the current element into the stack.
        stk.append(arr[i])

    # Returning the final vector after all the iterations.
    return ans
