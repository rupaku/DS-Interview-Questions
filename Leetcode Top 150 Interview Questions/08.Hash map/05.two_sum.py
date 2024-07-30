# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_mp={}
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in hash_mp:
                return [i,hash_mp[comp]]
            hash_mp[nums[i]]=i