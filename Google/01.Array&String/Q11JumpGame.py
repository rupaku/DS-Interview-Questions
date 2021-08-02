'''
https://leetcode.com/problems/jump-game/solution/
https://www.youtube.com/watch?v=muDPTDrpS28
find maximum index of reachable
start with 0th index , maxjump as its list value, maintain jump index.
If jump points to 0, thats the maximum reachable index.
If pointer crosses max reachble return False
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DP approach
        # lastpos=len(nums)-1
        # for i in range(len(nums)-1,-1,-1):
        #     if i+nums[i] >= lastpos:
        #         lastpos=i
        # return lastpos == 0
        #Peak approach
        reachable=0
        n= len(nums)
        for i in range(n):
            if reachable < i:
                return False
            reachable=max(reachable, i+nums[i])
        return True
            
        