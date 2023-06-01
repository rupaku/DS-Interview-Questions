'''https://leetcode.com/problems/palindrome-partitioning/description/'''
class Solution:
    def partition(self, nums: str) -> List[List[str]]:
        def is_pallin(nums,low,high):
            while low <= high:
                if nums[low] != nums[high]:
                    return False
                low=low+1
                high=high-1
            return True
        def backtrack(output,tempList,nums,start):
            if start == len(nums):
                output.append(list(tempList))
            else:
                for i in range(start,len(nums)):
                    if is_pallin(nums,start,i):
                        tempList.append(nums[start:i+1])
                        backtrack(output,tempList,nums,i+1)
                        tempList.pop()
        output=[]
        backtrack(output,[],nums,0)
        return output