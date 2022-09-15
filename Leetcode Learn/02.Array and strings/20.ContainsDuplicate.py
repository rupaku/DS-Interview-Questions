'''https://leetcode.com/problems/contains-duplicate/
time:  O(n)
space: O(n)
'''

class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     hashmap={}
    #     for i in nums:
    #         if i in hashmap:
    #             return True
    #         else:
    #             hashmap[i] = 1
    #     return False
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False
            

