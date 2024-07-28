# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def jump(self, nums: List[int]) -> int:
        reachable=0
        res=0
        end=0
        for i in range(len(nums)-1):
            reachable=max(reachable,i+nums[i])
            if reachable >= len(nums)-1:
                res=res+1
                break
            if i == end:
                res=res+1
                end=reachable
        return res
        