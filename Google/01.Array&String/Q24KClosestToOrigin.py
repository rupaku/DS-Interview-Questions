'''
Q: https://leetcode.com/explore/interview/card/google/59/array-and-strings/3062/
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3062/discuss/498448/Python-or-MaxHeap-tm

points = [[3,3],[5,-1],[-2,4]]
K = 2 
#output: [[-2, 4], [3, 3]]
'''

# from heapq import heapreplace, heapify
# class Solution(object):
#     def get_distance(self,points,nums):
#             for pair in points:
#                 x,y =pair #[1,2]
#                 dist = (x**2+y**2)**0.5
#                 nums.append((-dist,x,y))
                
#     def kClosest(self, points, K):
#         # points.sort(key=lambda P : P[0]**2 + P[1]**2)
#         # return points[:K]
#         nums=[]
#         self.get_distance(points,nums)
#         heap=nums[:K]
#         heapify(heap) # descending order distance
#         for i in range(K,len(nums)):
#             if (-nums[i][0] < -heap[0][0]):
#                 heapreplace(heap,nums[i])
                
#         res = []
#         for num, x, y in heap:
#             res.append([x, y])    
#         return res        
import heapq
from typing import List


class Solution:
    @staticmethod
    def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        i = 0
        res = []
        for n1, n2 in points:
            dist = (n1**2) + (n2**2)
            heapq.heappush(min_heap, (dist, n1, n2))

        while i < k:
            dist, n1, n2 = heapq.heappop(min_heap)
            res.append([n1, n2])
            i += 1
        return res

 
