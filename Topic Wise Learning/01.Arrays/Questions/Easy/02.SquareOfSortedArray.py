'''
https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Method 1  sort and square
        '''
        return sorted(x*x for x in nums)
        '''
    
        #Method 2 Two pointer
        # to iterate over the negative part in reverse, and the positive part in the forward direction.
        
        n= len(nums)
        res=[0]*n
        left=0
        right=n-1
        for i in range(n-1,-1,-1):
            if abs(nums[left]) < abs(nums[right]):
                square=nums[right]
                right=right-1
            else:
                square=nums[left]
                left=left+1
            res[i]=square*square
        return res
        