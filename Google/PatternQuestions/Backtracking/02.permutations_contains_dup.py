''''''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(output, tempList, nums):
            if len(tempList) == len(nums):
                output.append(tempList.copy())
            else:
                for i in range(len(nums)):
                    '''For Non duplicates'''
                    # if nums[i] in tempList:
                    #     continue
                    '''For duplicates'''
                    if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i - 1]):
                        continue
                    used[i] = True
                    tempList.append(nums[i])
                    backtrack(output, tempList, nums)
                    used[i] = False
                    tempList.pop()

        output=[]  
        used = [False] * len(nums) 
        backtrack(output, [], nums)
        return output


        