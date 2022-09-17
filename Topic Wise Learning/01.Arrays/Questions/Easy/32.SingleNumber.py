'''
https://leetcode.com/problems/single-number/submissions/
'''
class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     res=nums[0]
    #     for i in range(1,len(nums)):
    #         res=res^nums[i]
    #     return res
    def singleNumber(self, nums: List[int]) -> int:
        hash_table =defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        for i in hash_table:
            if hash_table[i] == 1:
                return i
obj=Solution()
nums=[2,2,1]
obj.singleNumber(nums)
        