'''
https://leetcode.com/problems/jewels-and-stones/submissions/
https://www.youtube.com/watch?v=C9JKUMYmgUA

put jewels into set
check each stones char with jewel set and return count
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set=set(jewels)
        return sum(s in jewels_set for s in stones)
        