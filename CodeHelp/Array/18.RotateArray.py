'''
https://leetcode.com/problems/rotate-array/
'''
class Solution:
    # def reverse(self,nums,start,end):
    #     while start < end:
    #         nums[start],nums[end]=nums[end],nums[start]
    #         start=start+1
    #         end=end-1
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     n=len(nums)
    #     k=k%n
    #     self.reverse(nums,0,n-1)
    #     self.reverse(nums,0,k-1)
    #     self.reverse(nums,k,n-1)
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        temp=[0]*n
        for i in range(len(nums)):
            temp[(i+k)%n] = nums[i]
            
        nums[:]=temp