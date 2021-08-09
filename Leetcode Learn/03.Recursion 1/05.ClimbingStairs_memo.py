'''
https://leetcode.com/problems/climbing-stairs/submissions/
'''
class Solution:
    def climb_recur(self,n,lookup):
        if n in lookup:
            return lookup[n]
        else:
            if n == 1:
                return 1
            elif n ==2:
                return 2
            else:
                result = self.climb_recur(n-1,lookup) + self.climb_recur(n-2,lookup)
            lookup[n]=result
        return result
        
    def climbStairs(self, n: int) -> int:
        memo={}
        return self.climb_recur(n,memo)
    
