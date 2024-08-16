# https://leetcode.com/problems/maximum-profit-in-job-scheduling


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        tuples = []

        for i in range(len(profit)):
            tuples.append((startTime[i], endTime[i], profit[i]))

        tuples.sort(key=lambda x: x[0]) #sort as per start time

        dp = [0] * (len(tuples) + 1)

        for i in range(len(tuples) - 1, -1, -1):
            nextIdx = self.binarySearch(tuples, i, tuples[i][1])
            dp[i] = max(tuples[i][2] + dp[nextIdx], dp[i + 1])

        return dp[0]

    def binarySearch(self, tuples: List[Tuple[int, int, int]], start: int, target: int) -> int:
        end = len(tuples) - 1

        while start <= end:
            m = start + (end - start) // 2
            if tuples[m][0] >= target:
                end = m - 1
            else:
                start = m + 1

        return start