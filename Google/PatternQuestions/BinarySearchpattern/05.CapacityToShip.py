'''https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/submissions/960115172/'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            day=1
            total=0
            for weight in weights:
                total=total+weight
                if total > capacity:
                    total=weight
                    day=day+1
                    if day > days:
                        return False
            return True
                

        l=max(weights)
        r=sum(weights)
        while l < r:
            mid=l+(r-l)//2
            if feasible(mid):
                r=mid
            else:
                l=mid+1
        return l