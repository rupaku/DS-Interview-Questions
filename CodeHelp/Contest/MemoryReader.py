'''
https://www.codingninjas.com/codestudio/contests/codestudio-weekend-contest/3114728/problems/14418?leftPanelTab=2
'''
'''
    Time Complexity: O(N ^ 2)
    Space Complexity: O(N ^ 2)

    where 'N' is the number of good memory points. 
'''

def memoryReader(memory):
    
    n = len(memory)
    
    # Initialize an unordered set to keep track of the possible jump lengths.
    dp=[set() for i in range (n)]
    
    # The first jump is always of length memory[0].
    dp[0].add(memory[0])
    
    for i in range (1, n):
        
        # Check all ways to reach this point.
        for j in range (i):
            
            jumpLength = memory[i] - memory[j]
            
            # Check if the jump is valid.
            if jumpLength in dp[j] or jumpLength - 1 in dp[j] or jumpLength + 1 in dp[j]:
                dp[i].add(jumpLength)
                
    # If there is any way to reach the last stone, the set is non empty.
    if len(dp[-1]):
        return "YES"
    
    return "NO"