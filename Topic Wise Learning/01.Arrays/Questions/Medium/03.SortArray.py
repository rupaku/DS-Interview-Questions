'''
https://leetcode.com/problems/sort-an-array/
'''

class Solution:
    def merge_sort(self,left_list,right_list):
        i=j=0
        res=[]
        print(left_list)
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                res.append(left_list[i])
                i=i+1
            else:
                res.append(right_list[j])
                j=j+1
                
        res.extend(left_list[i:])
        res.extend(right_list[j:])
        return res
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot=int(len(nums)/2)
        left_list=self.sortArray(nums[0:pivot])
        right_list=self.sortArray(nums[pivot:])
        return self.merge_sort(left_list, right_list)
        