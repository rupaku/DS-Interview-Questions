#https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain=0
        curr_gain=0
        ans=0

        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] -cost[i]

            #if met valley.start with next station with 0 gas
            if curr_gain < 0:
                curr_gain=0
                ans=i+1
        return ans if total_gain >= 0 else -1
        