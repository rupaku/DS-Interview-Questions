'''
https://www.codingninjas.com/codestudio/contests/codestudio-weekend-contest/3114728/problems/14460
'''
'''
    Time Complexity: O(n*log(n)).
    Space Complexity: O(1).

    where n is the number of guests.
'''
from typing import *

def maximumHandshakes(n: int, entry: List[int], exit: List[int])-> int:

    MOD = 1000000007
    
    # Sorting both entry and exit times.
    entry.sort()
    exit.sort()

    i = 0
    j = 0
    currentPerson = 0
    maximumPerson = 0

    # Iterating over all the guests.
    while i < n:

        # If current entry time is less than the current exit
        # time, incease the currentPerson by 1 and increase 'i'.
        while i < n and entry[i] < exit[j]:
            i += 1
            currentPerson += 1

        # Update maximumPerson as the maximum of 
        # itself and currentPerson.
        maximumPerson = max(maximumPerson, currentPerson)

        # If current entry time is greater than the 
        # current exit time, decrease the currentPerson
        # by 1 and increase 'j'.
        while i < n and entry[i] >= exit[j]:
            j += 1
            currentPerson -= 1

    # Calculate the number of handshakes when maximumPerson guests
    # are present.
    ans = ((maximumPerson*(maximumPerson - 1)) // 2) % MOD

    # Finally, return the ans.
    return ans