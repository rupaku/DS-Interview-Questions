'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

If the target that we're searching for has a value lower than the mid element, we discard the right half of the array i.e. end = mid - 1.
If the target that we're searching for has a value higher than the mid element, we discard the left half of the array i.e. begin = mid + 1.
If nums[mid] == element, then we found our target and we return from there.
'''
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         lower_bound = self.findBound(nums, target, True)
#         if lower_bound == -1:
#             return [-1,-1]
                    
#         upper_bound = self.findBound(nums, target, False)
#         return [lower_bound,upper_bound]
    
#     def findBound(self, nums: List[int], target:int,isFirst: bool) -> int:
#         n=len(nums)
#         begin =0
#         end=n-1
#         while begin <= end:
#             mid = int((begin+end)/2)
            
#             if nums[mid] == target:
#                 if isFirst:
#                     #lower bound first occurence
#                     if mid == begin or nums[mid-1] < target:
#                         return mid
#                     end=mid-1 # search on left
#                 else:
#                     #last occurence
#                     if mid == end or nums[mid+1] > target:
#                         return mid
#                     begin = mid+1
#             elif nums[mid] > target:
#                 end =mid-1
#             else:
#                 begin = mid+1
                
#         return -1

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        
        def searchLow(nums, target):
            l, h = 0, len(nums) - 1
            while l <= h:
                mid = (l + h)//2
                if nums[mid] >= target:
                    h = mid - 1
                else:
                    l = mid + 1
            return l
                
        def searchHigh(nums, target):
            l, h = 0, len(nums) - 1
            while l <= h:
                mid = (l + h)//2
                if nums[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1
            return h
        
        start = searchLow(nums, target)
        end = searchHigh(nums, target)
        if 0 <= start < len(nums) and start <= end and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]