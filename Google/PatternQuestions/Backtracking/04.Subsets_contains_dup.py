'''https://leetcode.com/problems/subsets/submissions/961444196/'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(self,output, tempList, nums, start):
                output.append(list(tempList))
                for i in range(start,len(nums)):
                    #For duplicates
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    #For duplicates
                    tempList.append(nums[i])
                    backtrack(self,output, tempList, nums, i+1)
                    tempList.pop()

        output=[]  
        backtrack(self,output, [], nums, 0)
        return output



