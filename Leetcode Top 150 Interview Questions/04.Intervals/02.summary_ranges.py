#https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output=[]
        for n in nums:
            if output and output[-1][1] == n-1:
                output[-1][1]=n
            else:
                output.append([n,n])
        return [f'{x}->{y}' if x!=y else f'{x}' for x, y in output]
        