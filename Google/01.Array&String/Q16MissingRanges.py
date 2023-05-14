'''
https://leetcode.com/problems/missing-ranges/solution/
if same num return lower else concatenate l-> u
prev =l-1
in range of nums if i <nums[i] get nums[i] else u++
if prev+1 <= curr -1 ->append to result ,otherwise prev=curr
'''
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def formatRange(lower,upper):
            if lower == upper:
                return [lower,lower]
            return [lower ,upper]
        
        res=[]
        prev =lower-1
        for i in range(len(nums)+1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= curr -1:
                res.append(formatRange(prev+1,curr-1))
            prev = curr
        return res