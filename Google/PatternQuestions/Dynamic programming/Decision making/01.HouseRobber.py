'''https://leetcode.com/problems/house-robber/submissions/968202601/?envType=list&envId=55af7bu7'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        rob_next_plus_one=0
        rob_next=nums[n-1]
        for i in range(n-2,-1,-1):
            curr=max(rob_next,rob_next_plus_one+nums[i])

            rob_next_plus_one = rob_next
            rob_next=curr

        return rob_next
