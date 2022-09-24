'''
https://www.codingninjas.com/codestudio/contests/codestudio-weekend-contest/3114728/problems/14694?leftPanelTab=0
'''
'''
    Time complexity: O(N)
    Space complexity: O(1)

    Where 'N' is the size of given array.
'''

from typing import *

def cherryBiscuit(a: List[int], n: int, k: int)-> int:

    # Variable for storing 'ans'.
    ans = 0

    for i in range(n):

        # Check if Ninja will like current Biscuit.
        if a[i] > k:
            ans += 1

    # Return the final answer.
    return ans