'''
https://www.codingninjas.com/codestudio/contests/codestudio-weekend-contest-1/3119366/problems/14758?leftPanelTab=0
'''
'''
	Time complexity: O(N)
	Space complexity: O(1)
	
	Where 'N' is the length of 'ARR'.
'''

from typing import *

def maxFXI(n: int, arr: List[int], k: int)-> int:

    # Variable to hold the required answer.
    val = 0

    for i in range(n):
        # Calculate the value of F(x) for 'arr[i]' as 'x'.
        fx = (2 * k) // (1 + 2 * abs(arr[i] - k))
        val = max(val, fx)
    
    return val