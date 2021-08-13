'''
https://leetcode.com/problems/permutations/submissions/
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first,n):
                #Place ith integer first in curr perm
                nums[first],nums[i]=nums[i],nums[first]
                #next integer to complete perm
                backtrack(first+1)
                #backtrack
                nums[first],nums[i]=nums[i],nums[first]
                
        n=len(nums)
        output=[]
        backtrack()
        return output
        