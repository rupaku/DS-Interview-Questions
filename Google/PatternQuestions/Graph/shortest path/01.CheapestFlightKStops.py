'''https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/'''
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # First create graph from flights
        adj = [[] for i in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))


        # initial config for source
        dist = [float('inf') for i in range(n)]
        dist[src] = 0
        # stop, node, distance
        q = [(0, src, 0)]
        heapq.heapify(q)

        # dijkstra algorithm
        while q:
            stop, node, distance = heapq.heappop(q)
            if stop > k:
                continue
            for it in adj[node]:
                adjNode = it[0]
                edgeWt = it[1]
                if edgeWt + distance < dist[adjNode] and stop <= k:
                    dist[adjNode] = edgeWt + distance
                    heapq.heappush(q, (stop + 1, adjNode, dist[adjNode]))


        # return destination distance
        return dist[dst] if dist[dst] != float('inf') else -1