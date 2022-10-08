'''
https://www.codingninjas.com/codestudio/contests/codestudio-weekend-contest-1/3119366/problems/14467?leftPanelTab=0
'''
'''
	Time Complexity: O(N * logN)
	Space Complexity: O(1)

	where 'N' is the number of tasks given in the problem.
'''

def possTasks(n, a, b, c):
    
    if a + b > n:
        return 0

    # Sorting the array
    c.sort()
    ans = c[n - a] - c[b - 1]
    return ans