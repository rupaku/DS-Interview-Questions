'''
https://leetcode.com/problems/3sum-with-multiplicity/
'''
#Need to be corrected
class Solution:
    def threeSumMulti(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        for i in range(0,len(nums)-2):
            temp=target-nums[i]
            low=i+1
            high=len(nums)-1
            while low < high:
                num=nums[low]+nums[high]
                if num == temp:
                    sc=1
                    ec=1
                    while low < high and nums[low] == nums[low+1]:
                        low=low+1
                        sc=sc+1
                    while low < high and nums[high] == nums[high-1]:
                        high=high-1
                        ec=ec-1
                    if low == high:
                        temp=(sc*(sc-1))//2
                        ans=(ans+temp)%10**9+7
                    else:
                        ans=ans+(sc*ec)%10**9+7
                    low=low+1
                    high=high-1
                elif num < target:
                    low=low+1
                else:
                    high=high-1
        return ans