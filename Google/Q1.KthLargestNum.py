'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/361/
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Approach 1
        # nums.sort()
        # return nums[::-1][k-1]
        #Approach 2
        return heapq.nlargest(k,nums)[-1]
        #Approach3 : qucikselect : find pivot and place it at end , rest num less than pivot and rearrange pivot

obj = Solution()
obj.findKthLargest([3,2,3,1,2,4,5,5,6],4)