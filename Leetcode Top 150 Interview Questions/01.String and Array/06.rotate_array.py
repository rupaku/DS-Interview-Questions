#https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        temp=[0]*n
        for i in range(len(nums)):
            temp[(i+k)%n] = nums[i]
            
        nums[:]=temp