#https://leetcode.com/problems/jump-game/submissions/1315876889/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        reachable=0
        for i in range(len(nums)):
            if reachable < i:
                return False
            reachable= max(reachable,i+nums[i])
        return True