'''
Q: https://leetcode.com/explore/interview/card/google/59/array-and-strings/3062/
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3062/discuss/498448/Python-or-MaxHeap-tm

points = [[3,3],[5,-1],[-2,4]]
K = 2 
#output: [[-2, 4], [3, 3]]
'''

from heapq import heapreplace, heapify
class Solution(object):
    def get_distance(self,points,nums):
            for pair in points:
                x,y =pair #[1,2]
                dist = (x**2+y**2)**0.5
                nums.append((-dist,x,y))
                
    def kClosest(self, points, K):
        # points.sort(key=lambda P : P[0]**2 + P[1]**2)
        # return points[:K]
        nums=[]
        self.get_distance(points,nums)
        heap=nums[:K]
        heapify(heap) # descending order distance
        for i in range(K,len(nums)):
            if (-nums[i][0] < -heap[0][0]):
                heapreplace(heap,nums[i])
                
        res = []
        for num, x, y in heap:
            res.append([x, y])    
        return res        
        
