'''
https://leetcode.com/problems/merge-sorted-array/
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Method 1 Merge and sort
        '''
        for i in range(n):
            nums1[i+m] = nums2[i]
            
        nums1.sort()
        '''
        
        #Method 2 Three pointer(Beginning)
        '''
        nums1_copy= nums1[:m]
        p1=0 # pointer for nums1copy
        p2=0 # pointer for nums2
        
        for p in range(n+m):
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1=p1+1
            else:
                nums1[p] = nums2[p2]
                p2=p2+1
        '''
        #Method 3 Three pointer(From End)
        p1=m-1
        p2=n-1
        
        for p in range(n+m-1,-1,-1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p]=nums1[p1]
                p1=p1-1
            else:
                nums1[p]=nums2[p2]
                p2=p2-1
