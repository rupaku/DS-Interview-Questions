'''https://leetcode.com/problems/permutations/'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(output, tempList, nums):
            if len(tempList) == len(nums):
                output.append(tempList.copy())
            else:
                for i in range(len(nums)):
                    if nums[i] in tempList:
                        continue
                    tempList.append(nums[i])
                    backtrack(output, tempList, nums)
                    tempList.pop()

        output=[]    
        backtrack(output, [], nums)
        return output


        