'''https://leetcode.com/problems/two-sum/description/'''

#Solution 1 [o(n^2, o(1)]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
            
# Solution 2 [o(n), o[n]]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_mp={}
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in hash_mp:
                return [i,hash_mp[comp]]
            hash_mp[nums[i]]=i