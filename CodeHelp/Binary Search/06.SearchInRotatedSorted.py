'''
https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
O(logn)
'''
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n=len(nums)-1
#         pivot=Solution.get_pivot(nums,target)
#         #check target is between pivot and n-1
#         if target >= nums[pivot] and target <= nums[n-1]:
#             #2nd line
#             return Solution.binary_search(nums,pivot,n-1,target)
#         else:
#             #1st line
#             return Solution.binary_search(nums,0,pivot-1,target)
#         return -1
    
#     def get_pivot(nums,target):
#         l=0
#         h=len(nums)-1
#         while l <= h:
#             mid=(l+h)//2
#             if nums[mid] >= nums[0]:
#                 l=mid+1
#             else:
#                 h=mid
#         return l
    
#     def binary_search(nums,s,e,target):
#         l=0
#         h=len(nums-1)
#         while l <= h:
#             mid=(l+h)//2
#             if target == nums[mid]:
#                 return mid
#             elif target >= nums[mid]:
#                 s=mid+1
#             else:
#                 e=mid-1
#         return mid
 class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1
        #Find Pivot
        left=0
        right=len(nums)-1
        while(left < right):
            mid=left+(right-left)//2
            if (nums[mid] > nums[right]):
                left=mid+1
            else:
                right=mid
               
        #check if target is between pivot and n-1
        start=left
        left=0
        right=len(nums)-1
        if (target >= nums[start] and target <= nums[right]):
            left=start
        else:
            right=start
        #binary search
        while(left <= right):
            mid=left+(right-left)//2
            if nums[mid] == target:
                return mid
            elif(nums[mid] < target):
                left=mid+1
            else:
                right=mid-1
        return -1       
                