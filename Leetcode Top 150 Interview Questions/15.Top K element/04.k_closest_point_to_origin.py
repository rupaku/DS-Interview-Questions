# https://leetcode.com/problems/k-closest-points-to-origin/

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

