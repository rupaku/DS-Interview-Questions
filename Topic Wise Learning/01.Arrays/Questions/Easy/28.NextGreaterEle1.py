'''
https://leetcode.com/problems/next-greater-element-i/submissions/
time  O(n)
space O(n)
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1hashIdx ={n:i for i,n in enumerate(nums1)}
        res = [-1] *len(nums1)
        stack=[]
        for i in range(len(nums2)):
            curr =nums2[i]
            #check curr is greater than top of stack
            while stack and curr > stack[-1]:
                val=stack.pop()
                idx =nums1hashIdx[val] #pick from hashmap
                res[idx] =curr
            if curr in nums1hashIdx: #if curr in hashmap
                stack.append(curr)
        return res
                