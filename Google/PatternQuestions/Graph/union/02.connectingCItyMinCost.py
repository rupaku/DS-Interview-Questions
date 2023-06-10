'''https://leetcode.com/problems/connecting-cities-with-minimum-cost/submissions/964896738/'''
from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        neighbor = defaultdict(list)
        #key(city): value((neighbor city, cost))
        #1:(2,5), (3,6) means city 1 to 2 is 5, to 3 is 6
        for i, j ,c in connections:
            neighbor[i].append((j,c))
            neighbor[j].append((i,c))
        
        res = 0
        #(cost, neibhor city)
        #set this default cost start from city 1 with value 0
        miniheap = [(0,1)]
        visited = set()
        while miniheap:
            c, i = heappop(miniheap)
            if i in visited:
                continue
            else:
                visited.add(i)
                res += c
                if len(visited) == N:
                    return res
                else:
                    for j, c in neighbor[i]:
                        if j in visited:
                            continue
                        else:
                            #since minheap will always put smallest value in front, so we compare c value
                            heappush(miniheap,(c, j))
        return -1 