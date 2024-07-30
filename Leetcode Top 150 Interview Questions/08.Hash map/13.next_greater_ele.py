#https://leetcode.com/problems/next-greater-element-i/editorial/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map ={n:i for i,n in enumerate(nums1)}
        #  result for [4,1,2] => {4: 0, 1: 1, 2: 2}
        print(map)
        res = [-1] *len(nums1)
        stack=[]
        for i in range(len(nums2)):
            curr =nums2[i]
            #check curr is greater than top of stack
            while stack and curr > stack[-1]:
                val=stack.pop()
                idx =map[val] #pick from hashmap
                res[idx] =curr
            if curr in map: #if curr in hashmap
                stack.append(curr)
        return res
                