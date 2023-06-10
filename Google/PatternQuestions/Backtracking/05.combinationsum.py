'''c'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(output,tempList,nums,target,start):
            if target < 0:
                return
            elif target == 0:
                output.append(list(tempList))
            else:
                for i in range(start,len(nums)):
                    tempList.append(nums[i])
                    backtrack(output,tempList,nums,target-nums[i],i)
                    tempList.pop()
        output=[]
        nums.sort()
        backtrack(output,[],nums,target,0)
        return output