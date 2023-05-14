'''
https://leetcode.com/problems/3sum/
low=i+1
high =last ele
current sum = nums[i]+nums[low]+nums[high]
if CS < 0 : low++
elif CS > 0: high --
else append in list low++,high --
'''
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res=[]
#         nums.sort()
#         for i,a in enumerate(nums):
#             if i > 0 and a == nums[i-1]:
#                 continue
#             l=i+1
#             r=len(nums)-1
#             while(l < r):
#                 threesum = a+nums[l]+nums[r]
#                 if threesum > 0:
#                     r=r-1
#                 elif threesum < 0:
#                     l=l+1
#                 else:
#                     res.append([a,nums[l],nums[r]])
#                     l=l+1
#                     while nums[l] == nums[l-1] and l < r:
#                         l=l+1
#         return res
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        dups=set()
        seen={}
        for i,v1 in enumerate(nums):
            if v1 not in dups:
                dups.add(v1)
            for j,v2 in enumerate(nums[i+1:]):
                complement=-v1-v2
                if complement  in seen and seen[complement] == i:
                    res.add(tuple(sorted((v1,v2,complement))))
                seen[v2] = i
        return res