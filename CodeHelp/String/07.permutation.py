'''
https://leetcode.com/problems/permutation-in-string/solution/
'''
from collections import Counter
d1 = Counter(s1)
k = len(s1)
for i in range(len(s2)):  # ---- O(n)
    sub = s2[i:i+k]  # ------ O(k)
    d2 = Counter(sub) # --- O(k)
    if d1 == d2:
        return True
return False