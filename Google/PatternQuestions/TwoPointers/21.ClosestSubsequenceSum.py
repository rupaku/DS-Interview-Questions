'''https://leetcode.com/problems/closest-subsequence-sum/description/'''
import bisect
class Solution:
    def solve(self,nums,i,val,sums):
        if i == len(nums):
            sums.append(val)
            return
        self.solve(nums,i+1,val+nums[i],sums)
        self.solve(nums,i+1,val,sums)
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        s1=[]
        s2=[]
        self.solve(nums[:n//2],0,0,s1)
        self.solve(nums[n//2:],0,0,s2)
        s2=sorted(s2)
        n2=len(s2)
        ans=float("inf")
        for s in s1:
            rem=goal-s
            i=bisect.bisect_left(s2,rem)
            if i < n2:
                ans= min(ans, abs(rem-s2[i]))
            if i > 0:
                ans=min(ans,abs(rem-s2[i-1]))
        return ans