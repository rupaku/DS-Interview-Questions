'''
https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

offer[i] =(quality[i] * expWage[captain])/quality[captain]

'''
# Greedy approach
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        from fractions import Fraction
        ans = float('inf')

        N = len(quality)
        for captain in range(N):
            # Must pay at least wage[captain] / quality[captain] per qual
            factor = Fraction(wage[captain], quality[captain])
            prices = []
            for worker in range(N):
                
                price = factor * quality[worker]
                if price < wage[worker]: continue
                prices.append(price)

            if len(prices) < K: continue
            prices.sort()
            ans = min(ans, sum(prices[:K]))

        return float(ans)
# Heap approach

from fractions import Fraction
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        return float(ans)