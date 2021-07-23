'''
https://leetcode.com/problems/two-sum/

hashmap: find target-current ele and store in hashmap, if  value in hashmap fetch index of element and hashmap value
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute force
        '''for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]'''
        #Hash map
        hashmp ={}
        for i in range(len(nums)):
            x= target-nums[i]
            if x in hashmp:
                return [i, hashmp[x]]
            hashmp[nums[i]] = i
        
        