# https://leetcode.com/problems/top-k-frequent-elements/description/

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        for i in nums:
            freq_table[i] = freq_table.get(i, 0) + 1
        if k == len(nums):
            return nums

        return heapq.nlargest(k,freq_table.keys(), key= freq_table.get)

        