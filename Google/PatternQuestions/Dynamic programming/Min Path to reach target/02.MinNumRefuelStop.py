'''https://leetcode.com/problems/minimum-number-of-refueling-stops/description/'''
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp=[startFuel]+[0]*len(stations)
        for i ,(location,capacity) in enumerate(stations):
            for j in range(i,-1,-1):
                if dp[j] >= location:
                    dp[j+1]=max(dp[j+1],dp[j]+capacity)
        for i,val in enumerate(dp):
            if val >= target:
                return i
        return -1