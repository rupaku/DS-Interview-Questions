'''
https://www.codingninjas.com/codestudio/contests/codestudio-weekend-contest/3114728/problems/14466?leftPanelTab=2
'''
'''
	Time Complexity: O(|S|)
	Space Complexity: O(1)

	where |S| is the length of the given string.
'''

def isPoss(mid, freq, n):
    reqN = 0
    if mid == 0:
        return False
    for i in freq:
        
        # Taking ceil of (i/mid).
        if i > 0:
            reqN += (i + mid - 1) // mid

    if reqN <= n:
        return True
    
    return False

def minScrolls(s, n):
    freq = [0 for i in range(26)]
    for c in s:
        freq[ord(c) - ord('a')] += 1
    
    l = 0
    r = 100000000
    ans = r

    while l <= r:
        mid = l + (r - l) // 2
        if isPoss(mid, freq, n):
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1

    return ans