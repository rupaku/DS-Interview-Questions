'''
https://www.codingninjas.com/codestudio/problems/minimum-cost-to-make-string-valid_1115770?leftPanelTab=1
'''
'''

    Time Complexity : O(|STR|)
    Space Complexity : O(|STR|)

    Where |STR| is the length of STR.

'''

from collections import deque

def findMinimumCost(str):
    n = len(str)
    
    # If lenght is odd then it is impossible to make str valid.
    if(n % 2 == 1):
        return -1

    # To store invalid parts.
    st = deque()

    for i in range(n):

        if(str[i] == '}' and len(st) != 0):

            if(st[len(st) - 1] == '{'):

                # Remove the valid part in the stack.
                st.pop()
            else:

                # Keep the invalid part in the stack.
                st.append(str[i])
        else:
            # Keep the invalid part in the stack.
            st.append(str[i])
    
    p, q = 0, 0

    # Calculate the opening and closing brackets
    while(len(st) != 0):

        if(st[len(st) - 1] == '{'):
            p += 1

        else:
            q += 1

        st.pop()

    return ((p + 1) // 2) + ((q + 1) // 2)