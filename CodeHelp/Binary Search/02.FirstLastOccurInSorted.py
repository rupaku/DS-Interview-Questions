'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.findBound(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]
    
    
    def findBound(self, nums, target, isFirst):
        n = len(nums)
        begin, end = 0, n - 1
        
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                if isFirst:
                    if mid == begin or nums[mid-1] < target:
                        return mid
                    end = mid - 1 #first occur
                    
                else:
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    begin = mid + 1 #second occur
                    
            elif nums[mid] > target:
                end = mid - 1
            
            else:
                begin = mid + 1
                
        return -1

#otal num of occurence = (last occ - first occ) +1